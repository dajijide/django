# file:music/urls.py

'''此模块实现music应用中的子路由配置'''
from django.conf.urls import url
from . import views
from django.urls import path,re_path


urlpatterns = [
    # url('page1',views.page1_view),
    # url('page2',views.page2_view),
    re_path(r'^index',views.index_view),
]