#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/8 20:15
# @Author  : Nana Xing
# @File    : forms.py
# @ProjectName: myDjangoProject
# @Software : PyCharm
# @Description :
from django.forms import forms

from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        # 表明这个表单对应的数据库模型是 Comment 类
        model=Comment
        # 指定了表单需要显示的字段
        fields=['name','email','url','text']
