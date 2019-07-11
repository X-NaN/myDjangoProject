import markdown
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from comments.forms import CommentForm
from .models import Post, Category


# Create your views here.


def index(request):
    """
    首页，视图函数
    :param request:
    :return:
    """
    # return HttpResponse('欢迎访问我的博客首页')
    # return render(request,'blog/index.html',context={'title':'NaNa的博客首页','welcome':'欢迎访问我的博客首页'})
    # 逆序,- 号表示逆序
    # post_list = Post.objects.all().order_by('-create_time')
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    """
    文章详情视图函数
    :param request:
    :param pk: 文章id，是从url提取出来的，提取规则在url模式中（正则表达式）
    :return:
    """
    # 获取文章
    post = get_object_or_404(Post, pk=pk)

    # 浏览量+1
    post.increase_views()

    # 把 Markdown 文本转为 HTML 文本再传递给模板
    post.body = markdown.markdown(post.body, extensions=[
        'extra',
        'codehilite',
        'toc',
    ])

    # 表单
    form = CommentForm()
    # 文章评论列表
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }
    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    """
    归档，根据年月查询文章列表
    :param request:
    :param year:
    :param month:
    :return:
    """
    post_list = Post.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    """
    分类，查询分类下的文章列表
    :param request:
    :param pk: 分类Id
    :return:
    """
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

class IndexView(ListView):
    """
    首页类视图
    功能等于视图函数index()
    """
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'


class ArchivesView(ListView):
    """
    归档类视图
    """
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        year=self.kwargs.get('year')
        month=self.kwargs.get('month')
        post_list=super(ArchivesView,self).get_queryset().filter(create_time__year=year, create_time__month=month)
        return post_list

class CategoryView(ListView):
    """
    分类 类视图
    """
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        # 从 URL 捕获的命名组参数值保存在实例的 kwargs 属性（是一个字典）里
        cate=get_object_or_404(Category,pk=self.kwargs.get('pk'))# pk是分类id
        # get_queryset 方法获得全部文章列表
        return super(CategoryView,self).get_queryset().filter(category=cate)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self,request,*args,**kwargs):
        # 重写get方法
        # 当父类get方法被调用后，self.object有值，值为Post模型实例，即被访问的文章post
        response=super(PostDetailView,self).get(request,*args,**kwargs)

        self.object.increase_views()
        # 视图必须返回一个 HttpResponse 对象
        return response

    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post=super(PostDetailView,self).get_object(queryset=None)
        # 把 Markdown 文本转为 HTML 文本再传递给模板
        post.body = markdown.markdown(post.body, extensions=[
            'extra',
            'codehilite',
            'toc',
        ])
        return post

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
        # 还要把评论表单、post 下的评论列表传递给模板。
        context=super(PostDetailView,self).get_context_data(**kwargs)
        form=CommentForm()
        comment_list=self.object.comment_set.all()
        context.update({
            'form':form,
            'comment_list':comment_list
        })
        return context


