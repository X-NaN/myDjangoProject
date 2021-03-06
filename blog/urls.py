#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/6/6 17:57
# @Author  : Nana Xing
# @File    : urls.py
# @ProjectName: myDjangoProject
# @Software : PyCharm
# @Description :url和对应的视图函数，开发流程：首先配置 URL，即把相关的 URL 和视图函数绑定在一起，然后实现视图函数，编写模板并让视图函数渲染模板。

# 从当前目录下导入 views 模块
from django.urls import path

from . import views

app_name = 'blog'  # 视图函数命名空间,标识这个 URL 模块是属于 blog 应用的
urlpatterns = [
    # url(r'^$',views.index,name='index')
    path(r'', views.IndexView.as_view(), name='index'),
    # 命名捕获组,并作为关键字参数传给其对应的视图函数 detail
    path(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    # path(r'^category/(?<pk>[0-9]+)/$', views.category, name='category'),
    path(r'^category/(?<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
]
