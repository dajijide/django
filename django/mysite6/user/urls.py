from . import views
from django.urls import re_path,path
from django.conf.urls import url

urlpatterns = [
    re_path(r'^reg$',views.reg_view),
    re_path(r'^login$',views.log_view),
    re_path(r'^logout$',views.logout_view),
    re_path(r'^reg2$',views.reg2_view)
]