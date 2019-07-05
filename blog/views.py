import markdown
from django.shortcuts import render, get_object_or_404

from .models import Post, Category


# Create your views here.


def index(request):
    """
    视图函数
    :param request:
    :return:
    """
    # return HttpResponse('欢迎访问我的博客首页')
    # return render(request,'blog/index.html',context={'title':'NaNa的博客首页','welcome':'欢迎访问我的博客首页'})
    # 逆序,- 号表示逆序
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    """
    文章详情视图函数
    :param request:
    :param pk: 文章id，是从url提取出来的，提取规则在url模式中（正则表达式）
    :return:
    """
    post = get_object_or_404(Post, pk=pk)
    # 把 Markdown 文本转为 HTML 文本再传递给模板
    post.body = markdown.markdown(post.body, extensions=[
        'extra',
        'codehilite',
        'toc',
    ])
    return render(request, 'blog/detail.html', context={'post': post})


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
