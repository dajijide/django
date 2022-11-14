from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models
# Create your views here.

# file :bookstore/views.py

def add_view(request):
    if request.method == 'GET':
        return render(request,'bookstore/add_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = request.POST.get('price')
        market_price = request.POST.get('market_price')
        try:
            models.Book.objects.create(title=title,
                                       pub=pub,
                                       price=price,
                                       market_price=market_price)
            return HttpResponseRedirect('/bookstore/all')
        except:
            return HttpResponse("添加失败!")
    return HttpResponseRedirect('/bookstore/all')

def show_all(request):
    books=models.Book.objects.all()
    # books=models.Book.objects.filter(price__gt=50)
    # books=models.Book.objects.exclude(pub__contains='清华大学',market_price__lt=40)
    # for abook in books:
    #     print("书名："+abook.title)
    return render(request,'bookstore/show_books.html',locals())


def mod_view(request,id):
    try:
        abook = models.Book.objects.get(id=id)
    except:
        return HttpResponse("没有id为" + id + "的数据记录")
    if request.method == 'GET':
        return render(request,'bookstore/mod.html',locals())
    elif request.method == 'POST':
        m_price=request.POST.get('market_price','0')
        abook.market_price = float(m_price)
        abook.save()
        return HttpResponseRedirect('/bookstore/all')


def del_view(request,id):
    try:
        abook = models.Book.objects.get(id=int(id))
    except Exception as err:
        return HttpResponse("删除失败!")
    abook.delete()
    return HttpResponseRedirect('/bookstore/all')


def select_low(request):
    if request.method == 'GET':
        return render(request,'bookstore/select_low.html',locals())
    elif request.method == 'POST':
        price = request.POST.get('price','0')
        abook = models.Book.objects.filter(price__lt=price)
        return render(request, 'bookstore/show_select.html', locals())


def set_cookies_view(request):
    resp = HttpResponse('OK')
    resp.set_cookie('myvar',100,max_age=1000000)
    # resp.delete_cookie('myvar')
    return resp

def get_cookies_view(request):
    # 获取cookies的值
    v = request.COOKIES.get('myvar')
    return HttpResponse('myvar=' +v)