from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from blog.models import Post
from comments.forms import CommentForm


def post_comment(request, post_pk):
    # 获取评论的文章
    post = get_object_or_404(Post, pk=post_pk)
    # HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求
    if request.method == 'POST':
        # 创建表单实例（）用户数据在request.POST中
        form = CommentForm(request.POST)

        if form.is_valid():  # 数据合法
            # 创建Comment模型类实例,commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment = form.save(commit=False)
            # 关联文章
            comment.post = post
            # 保证评论数据至数据库
            comment.save()

            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post': post, 'form': form, 'comment_list': comment_list}

            # 重新渲染详情页
            return render(request, 'blog/detail.html', context=context)

    # 不是POST请求，说明用户没有提交数据，重定向到文章详情页
    return redirect(post)
