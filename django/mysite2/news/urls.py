# file:news/urls.py

'''此模块实现music应用中的子路由配置'''
from django.conf.urls import url
from . import views
from django.urls import path,re_path


urlpatterns = [
    re_path(r'index',views.index_view),
]