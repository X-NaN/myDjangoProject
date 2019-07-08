from django.db import models

# Create your models here.

class Comment(models.Model):
    verbose_name = '评论'
    verbose_name_plural = '评论管理'
    name=models.CharField(max_length=100,verbose_name='用户名')
    email=models.EmailField(max_length=255,verbose_name='邮箱')
    url=models.URLField(blank=True,verbose_name='个人网站')
    text=models.TextField(verbose_name='评论内容')
    # 评论创建时间,auto_now_add 的作用是，当评论数据保存到数据库时，自动把 created_time 的值指定为当前时间
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='评论时间')

    # 一篇文章有多个评论，一个评论只属于一个文章
    post=models.ForeignKey('blog.Post',on_delete=models.CASCADE)
