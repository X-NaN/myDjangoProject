from django.shortcuts import render
from .models import Post

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
    post_list=Post.objects.all().order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

