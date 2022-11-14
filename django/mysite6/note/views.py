from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from user.models import User
from .models import Note
from django.db import models
from django.core.paginator import Paginator  # 导入分页类

def check_login(fn):
    def wrap(request, *args, **kwargs):
        if not hasattr(request, 'session'):  # 没有登录
            return HttpResponseRedirect('/user/login')
        if 'user' not in request.session:
            return HttpResponseRedirect('user/login')
        return fn(request, *args, **kwargs)

    return wrap


def list_view2(request):
    if not hasattr(request, 'session'):  # 没有登录
        return HttpResponseRedirect('/user/login')
    if 'user' not in request.session:
        return HttpResponseRedirect('user/login')
    # 此时一定登录
    user_id = request.session['user']['id']
    # 根据已登录的用户id找到当前登录的用户
    auser = User.objects.get(id=user_id)
    notes = auser.note_set.all()
    # 在此添加分页功能
    paginator = Paginator(notes,5)
    # 作用得到当前的页码数
    cur_page = request.GET.get('page','1')
    cur_page = int(cur_page)
    page = paginator.page(cur_page)
    return render(request, 'note/listpage.html', locals())


@check_login
def add_view(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        # 得到当前用户的信息
        user_id = request.session['user']['id']
        auser = User.objects.get(id=user_id)
        anote = Note(user=auser)
        anote.title = title
        anote.content = content
        anote.save()
        return HttpResponseRedirect('/note')

@check_login
def mod_view(request,id):
    # 得到当前登录的用户的模型对象
    user_id = request.session['user']['id']
    auser = User.objects.get(id=user_id)
    anote = Note.objects.get(user=auser,id=id)
    if request.method == 'GET':
        return render(request,'note/mod_note.html',locals())
    elif request.method == 'POST':
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        anote.title = title
        anote.content = content
        anote.save()
        return HttpResponseRedirect('/note/')

def del_view(request,id):
    user_id = request.session['user']['id']
    auser = User.objects.get(id=user_id)
    anote = Note.objects.get(user=auser, id=id)
    anote.detele()
    return HttpResponseRedirect('/note')