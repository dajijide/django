import http
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
# flie: music/views.py


def page1_view(request):
    return HttpResponse("页面1")


def page2_view(request):
    return HttpResponse("页面2")


def page3_view(request):
    return HttpResponse("页面3")


def index_view(request):
    return HttpResponse('音乐首页')