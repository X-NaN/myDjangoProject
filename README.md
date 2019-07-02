#myDjangoProject
***
##python+django搭建web项目

以下都是跟着Django教程：https://www.zmrenwu.com/courses/django-blog-tutorial/
在此记录一下。

一、开发环境：
win10+pycharm+虚拟环境

1. 创建虚拟环境：
venv_django

可以参考博客：https://blog.csdn.net/Nancy50/article/details/90897365
2. 安装django（2.2.2）
pip install django
3. 安装mysql数据库驱动
pip install mysqlclient

二、创建django项目
1. 创建django项目
>方法一：通过django命令

django-admin startproject blogproject

>方法二：通过Pycharm创建django项目

    1) 首先配置虚拟环境
    2) 创建django项目：
        File->New Project->选择Django

2. 运行django项目，看是否创建成功

    1) 运行django项目

        * 方法一：django命令
            python manage.py runserver
        * 方法二：Pycharm点击绿色三角按钮运行
    2) 浏览器打开：http://127.0.0.1:8000/

3. 创建blog应用
    1) 激活虚拟环境
    2) 进入到 manage.py 文件所在的目录下   
    3) 运行命令： python manage.py startapp blog ，即可建立一个 blog 应用

4. 创建 Django 博客的数据库模型

    编写models代码

5. 迁移数据库

django命令，迁移数据库步骤：

    1) 激活虚拟环境
    2) 进入到 manage.py 文件所在的目录下
    3) 运行命令：
        # Django 在 blog 应用的 migrations\ 目录下生成了一个 0001_initial.py 文件，这个文件是 Django 用来记录我们对模型做了哪些修改的文件。
        a. python manage.py makemigrations 
        # 让 Django 真正地为我们创建数据库表
        b. python manage.py migrate
    4) 查看django翻译的数据库表创建语句
        python manage.py sqlmigrate blog 0001

6. django 博客首页视图(初级版)

    1) 在blog应用目录下创建urls.py文件,并绑定url和视图函数  
    2) 在blog的views.py文件中编写视图函数index   
    3) 配置项目url：将blog应用的urls.py包含到项目的urls.py(即 settings.py 文件所在的目录下),url(r'', include('blog.urls'))  
    4) django模板系统：
    
        a. 在templates下创建blog文件夹
        b. 在blog 目录下建立一个名为 index.html
        c. 在 settings.py 文件里设置一下模板文件templates所在的路径

7. django 博客首页视图(高级版)


8. django admin 后台
    1. 创建超级管理员admin
    user:admin
    pwd:123456
    执行命令：python manage.py createsuperuser
    
    2. 在blog应用下的admin.py中注册模型，然后刷新url
     http://127.0.0.1:8000/admin
    > admin.site.register(Post)
    
    > admin.site.register(Category)
    
    > admin.site.register(Tag)
   
    3. 定制后台显示
     http://127.0.0.1:8000/admin/blog/post/
    > admin.site.register(Post,PostAdmin)

9. 文章详情页
    1. 模板页base.html
    2. index.html和detail.html继承模板页
    3. 占位标签 {% block main %},index.html通过占位标签main，填充网页不同的部分
    4. Post中生成文章url
    

10. 代码高亮
    1. 安装markdown和Pygments
    2. 修改视图函数detail,将数据库取出的body，从 Markdown 文本转为 HTML 文本再传递给模板
    3. detail.html中的post.body增加过滤器，否则django把html文本原样输出
   

