# file : bookstore/url.py
from django.conf.urls import url
from django.urls import re_path,path
from . import views
urlpatterns = [
    re_path(r'^add_book',views.add_view),
    re_path(r'^add_author',views.add_view2),
]