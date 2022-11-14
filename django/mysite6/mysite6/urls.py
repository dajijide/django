"""mysite6 URL Configuration

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
from index.views import index_view,test_view
from django.contrib import admin
from django.urls import path,re_path
from django.urls import include
from django.conf.urls import url
from index.views import upload_view

# import sys,os
# sys.path.append(os.path.dirname(os.path.dirname(__file__))
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^user/',include('user.urls')),
    re_path(r'^$',index_view),
    re_path(r'^note/',include('note.urls')),
    re_path(r'^test',test_view),
    re_path(r'^upload',upload_view)
]
