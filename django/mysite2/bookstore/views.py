from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

# file :bookstore/views.py

def add_view(request):
    try:
        # 方法一
        abook = models.Book.objects.create(
            title= 'Python',price=20,pub='清华大学出版社',market_price=25)
        abook = models.Book.objects.create(
            title='Python3', price=60, pub='清华大学出版社',market_price=65)
        abook = models.Book.objects.create(
            title='Django', price=70, pub='清华大学出版社', market_price=75)
        abook = models.Book.objects.create(
            title='JQuery', price=90, pub='机械工业出版社', market_price=85)
        abook = models.Book.objects.create(
            title='Linux', price=80, pub='机械工业出版社', market_price=65)
        abook = models.Book.objects.create(
            title='Windows', price=50, pub='机械工业出版社', market_price=35)
        abook = models.Book.objects.create(
            title='HTML5', price=90, pub='清华大学出版社', market_price=105)
        # 方法二
        # abook = models.Book(price=98)
        # abook.title = '西游记'
        # abook.save() # 真正调用sql语句
        return HttpResponse("添加图书成功")
    except Exception as err:
        return HttpResponse("添加图书失败")

def add_view2(request):
    try:
        author = models.Author.object.create(
            name='王老师',age = 28,email = 'wangweichao@tedu.cn')
        author = models.Author.object.create(
            name='吕老师', age=31, email='lvze@tedu.cn')
        author = models.Author.object.create(
            name='祁老师', age=28, email='qitx@tedu.cn')
        return HttpResponse('添加作者成功')
    except Exception as err:
        return HttpResponse('添加作者失败')