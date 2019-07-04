#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/4 19:21
# @Author  : Nana Xing
# @File    : blog_tags.py
# @ProjectName: myDjangoProject
# @Software : PyCharm
# @Description :自定义模板标签:
# 1、定义模板标签函数
# 2、注册模板标签函数为模板标签@register.simple_tag
from django import template

from blog.models import Post, Category

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    """
    获取数据库最新5片文章
    :param num:
    :return:
    """
    return Post.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def archives():
    """
    文章按月归档
    :return:
    """
    return Post.objects.dates('create_time','month',order='DESC')

@register.simple_tag
def get_categories():
    """
    获取文章分类
    :return:
    """
    return Category.objects.all()
