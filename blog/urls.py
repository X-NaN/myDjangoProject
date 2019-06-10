#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/6/6 17:57
# @Author  : Nana Xing
# @File    : urls.py
# @ProjectName: myDjangoProject
# @Software : PyCharm
# @Description :url和对应的视图函数

from django.conf.urls import url
# 从当前目录下导入 views 模块
from django.urls import path

from  . import views

urlpatterns=[
    # url(r'^$',views.index,name='index')
    path(r'',views.index,name='index')
]