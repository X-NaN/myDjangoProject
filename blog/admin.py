from django.contrib import admin

# Register your models here.
from blog.models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','modified_time','category','author']

#在admine后台 注册模型
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)