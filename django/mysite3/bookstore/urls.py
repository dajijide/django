# file : bookstore/url.py
from django.conf.urls import url
from django.urls import re_path,path
from . import views
urlpatterns = [
    re_path(r'^add',views.add_view),
    re_path(r'^all',views.show_all),
    re_path(r'^mod/(\d+)',views.mod_view),
    re_path(r'^del/(\d+)',views.del_view),
    re_path(r'^select_low',views.select_low),
    re_path(r'^set_cookie',views.set_cookies_view),
    re_path(r'^get_cookie',views.get_cookies_view),
]