# file:mysite1/views.py


import http
from django.shortcuts import render, HttpResponse, HttpResponseRedirect


def index_view(resquest):
    html = "这是主页"
    return HttpResponse(html)


def page1_view(request):
    html = "<h1>这是第一个页面<h1>"
    return HttpResponse(html)


def page2_view(request):
    html = "<h1>这是第二个页面<h1>"
    return HttpResponse(html)


def pagen_view(request, n):
    html = "<h1>这是第%s个页面<h1>" % n
    return HttpResponse(html)


def math_view(request, x, op, y):
    x = int(x)
    y = int(y)
    result = None
    if op == 'add':
        result = x + y
    elif op == 'sub':
        result = x - y
    elif op == 'mul':
        result = x * y
    if result is None:
        return HttpResponseRedirect("https://www.baidu.com")
    html = "结果是:" + str(result)
    html += '您的ip地址是:' + request.META['REMOTE_ADDR']
    print(html)
    return HttpResponse(html)


def person_view(request, **kwargs):
    s = str(kwargs)
    return HttpResponse(s)


def birthday_view(request, y, m, d):
    html = '生日:' + y + '年' + m + '月' + d + '日'
    return HttpResponse(html)


def mypage_view(request):
    """
    此视图函数用来示意得到GET请求中的查询参数
    http://127.0.0.1:8000/mypage?a=100&b=200
    """
    if request.method == 'GET':
        # a = request.GET['a']
        # a = request.GET.get['a', '没有对应的值']
        a = request.GET.getlist('a')
        html = "a =" + str(a)
        b = request.GET.getlist('b')
        html += 'b =' + str(b)
        return HttpResponse(html)
    else:
        return HttpResponse('当前不是GET请求')


def sum_view(request):
    if request.method == 'GET':
        start = request.GET.get('start', '0')
        start = int(start)
        stop = request.GET['stop']
        stop = int(stop)
        step = request.GET.get('step', '1')
        step = int(step)
        mysum = sum(range(start, stop, step))
        html = '和是:%d' % mysum
        return HttpResponse(html)


login_form_html = """
<form action="/login" method="post">
    用户名:<input name="username" type="text">
    <input type="submit" value="登录">
</form>
"""


def login_view(request):
    if request.method == 'GET':
        return HttpResponse(login_form_html)
    elif request.method == 'POST':
        name = request.POST.get('username', '属性错误')
        html = "姓名:" + name
        return HttpResponse(html)


def login2_view(request):
    if request.method == 'GET':
        # 返回模板生成的html给浏览器
        # 方法一
        # 1.先加载模块
        # from django.template import loader
        # t = loader.get_template('mylogin.html')
        # # # 2.用模板生成html
        # html = t.render({"name":"sjia"})
        # # # 3.将html返回给浏览器
        # return HttpResponse(html)

        # 方法二
        return render(request, 'mylogin.html', {"name": 'sjia'})


def mytemp_view(request):
    # dic = {
    #     'x': 10
    # }
    x = -5
    return render(request, 'mytemp.html', locals())


def test_view(request):
    if request.method == 'GET':
        return render(request, 'test.html')
    elif request.method == 'POST':
        x = int(request.POST.get("x", 0))
        y = int(request.POST.get("y", 0))
        op = request.POST.get('op')
        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
        return render(request, 'test.html', locals())


def for_view(request):
    lst = ["北京", "上海", "天津", "重庆"]
    S = "Hello World!"
    n = 100
    return render(request, 'test_for.html', locals())


def index_view(request):
    return render(request, 'base.html')


def sport_view(request):
    return render(request,'sport.html')


def news_view(request):
    pass
