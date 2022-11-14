"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.urls import re_path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^$", views.page_view),
    path('page2/',views.page2_view),
    re_path(r"^page(/d+)", views.page1_view),
    re_path(r'^shebao$', views.shebao_view),
    re_path(r'^music/',include('music.urls')),
    re_path(r'^index/',include('index.urls')),
    re_path(r'^sport/',include('sport.urls')),
    re_path(r'^news/',include('news.urls')),
    re_path(r'^bookstore/',include('bookstore.urls')),
]
