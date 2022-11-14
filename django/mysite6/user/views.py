from django.shortcuts import render
from . import models
from django.http import HttpResponse, HttpResponseRedirect
# 导入django的User模型类
from django.contrib.auth.models import User

# Create your views here.
def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        # myform = forms.MyRegFrom(request.POST)
        # if myform.is_valid():
        #     dic = myform.cleaned_data
        #     username = dic['username']
        #     password1 = dic['password']
        #     password2 = dic['password2']
        #     return HttpResponse(str(dic))
        # else:
        #     return HttpResponse("表单验证失败")
        username = request.POST.get('username', '')
        password1 = request.POST.get('password_1', '')
        password2 = request.POST.get('password_2', '')

        # 验证数据合法性
        if len(username) < 6:
            username_error = '用户名太短！'
            return render(request, 'user/register.html', locals())
        # 验证密码1不能为空
        elif password1 == 0:
            password_1_error = '密码不能为空'
            return render(request, 'user/register.html', locals())

        # 验证两次密码必须一致
        elif password1 != password2:
            password_2_error = '两次密码不一样'
            return render(request, 'user/register.html', locals())

        # 检查数据库是否一有username这条记录,如果没有则完成注册
        try:
            auser = User.objects.get(username=username)
            username_error = "用户名已经存在"
            return render(request, 'user/register.html', locals())
        except:
            auser = User.objects.create_superuser(username=username, password=password1)
            html = '注册成功! <a href="/user/login">进入登录</a>'
            resp = HttpResponse(html)
            resp.set_cookie("username", username)
            return resp
        # try:
        #     auser = models.User.objects.get(username=username)
        #     username_error = "用户名已经存在"
        #     return render(request, 'user/register.html', locals())
        # except:
        #     auser = models.User.objects.create(username=username, password=password1)
        #     html = '注册成功! <a href="/user/login">进入登录</a>'
        #     resp = HttpResponse(html)
        #     resp.set_cookie("username", username)
        #     return resp


def log_view(request):
    if request.method == 'GET':
        username = request.COOKIES.get('username', '')
        return render(request, 'user/login.html', locals())
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == '':
            username_error = '用户名不能为空'
            return render(request, 'user/login.html', locals())
        # 设置session的值
        # request.session['abc'] = 123
        # se = request.session.get('abc')
        # print(se)
        # return HttpResponse("添加成功")

        try:
            auser = User.objects.get(username=username)
            # 记录一个登录状态
            if auser.check_password(password):
                request.session['user'] = {
                    'username': username,
                    'id': auser.id  # 记录当前用户的id
                }
                resp = HttpResponseRedirect('/')
                if 'remember' in request.POST:  # 选中状态
                    resp.set_cookie('username', username)
                return resp
            else:
                password_error = '密码错误'
                return render(request,'user/login.html',locals())
        except:
            password_error = "用户密码不正确"
            return render(request, 'user/login.html', locals())

        # try:
        #     auser = models.User.objects.get(username=username, password=password)
        #     # 记录一个登录状态
        #     request.session['user'] = {
        #         'username': username,
        #         'id': auser.id  # 记录当前用户的id
        #     }
        #     resp = HttpResponseRedirect('/')
        #     if 'remember' in request.POST:  # 选中状态
        #         resp.set_cookie('username', username)
        #     return resp
        # except:
        #     password_error = "用户密码不正确"
        #     return render(request, 'user/login.html', locals())


def logout_view(request):
    # 退出登录
    if 'user' in request.session:
        del request.session['user']  # 清楚登录记录
    return HttpResponseRedirect('/')  # 返回主页


from . import forms


def reg2_view(request):
    myform = forms.MyRegFrom()
    return render(request,'user/reg2.html',locals())
    # html = myform.as_p()
    # print(html)
    # return HttpResponse(html)