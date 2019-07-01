#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/6/6 09:48
# @Author  : Nana Xing
# @File    : models.py
# @ProjectName: myDjangoProject
# @Software : PyCharm
# @Description : 博客模型代码，对应blog应用的数据库表
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    """
    文章分类，一篇文章对应一个分类
    Django 要求模型必须继承models.Model类
    model类和数据库对应关系：
    一个 Python 类对应一个数据库表格，类名即表名，类的属性对应着表格的列，属性名即列名。
    Django 就可以把类翻译成数据库的操作语言，如Category，django会在数据库里创建一个名为 category 的表格，这个表格的一个列名为 name。还有一个列 id，Django 则会自动创建。
    models的CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
    Django 内置的全部类型可查看文档：
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """

    def __str__(self):
        return 'name:%s' % self.name

    # 分类名
    name = models.CharField(max_length=100)


class Tag(models.Model):
    """
    文章标签，一篇文章对应多个标签
    """

    def __str__(self):
        """
        对象描述
        :return:字符串
        """
        return 'name:%s' % self.name

    # 标签名
    name = models.CharField(max_length=100)


class Post(models.Model):
    """
    文章表
    """

    def __str__(self):
        return self.title

    # 文章标题
    title = models.CharField(max_length=70)

    # 文章正文 使用TextField 存储大段文本
    body = models.TextField()

    # 文章创建时间
    create_time = models.DateTimeField()
    # 文章最后一次修改时间
    modified_time = models.DateTimeField()

    # 文章摘要，可以为空
    excerpt = models.CharField(max_length=200, blank=True)

    # 文章分类，把文章对应的数据库表和分类对应的数据库表关联起来
    # 一个分类下有多个文章，一个文章对应一个分类。一对多的关系，用外键
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # 文章标签，把文章对应的数据库表和标签对应的数据库表关联起来
    # 一篇文章对应多个标签，一个标签对应多个文章。多对多的关系
    # 文章可以没有标签，可以为空
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth.models 是django内置的应用，专门用于处理网站用户的注册、登录等流程
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})


