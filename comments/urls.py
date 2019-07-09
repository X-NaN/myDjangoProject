#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/9 19:57
# @Author  : Nana Xing
# @File    : urls.py
# @ProjectName: myDjangoProject
# @Software : PyCharm
# @Description :
from django.urls import path

from comments import views

app_name = 'comments'  # 视图函数命名空间
urlpatterns = [
    # 命名捕获组,并作为关键字参数传给其对应的视图函数 detail
    path(r'^comment/post/(?<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),


]