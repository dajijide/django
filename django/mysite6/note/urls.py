from django.conf.urls import url
from . import views
from django.urls import re_path,path
urlpatterns = [
    # re_path(r'^$',views.list_view),
    re_path(r'^$',views.list_view2),
    re_path(r'^add',views.add_view),
    re_path(r'^mod/(\d+)',views.mod_view),
    re_path(r'^del/(\d+)',views.del_view),



]