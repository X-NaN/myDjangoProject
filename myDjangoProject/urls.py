"""myDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 将blog应用下的urls.py文件包含进来
    # http://127.0.0.1:8000/blog/#
    # path(r'blog/',include('blog.urls')),
    # http://127.0.0.1:8000
    path(r'', include('blog.urls')),
    path(r'',include('comments.urls'))
    # re_path(r'^message_form/$', getform),  # 正则表达的这么写
]
