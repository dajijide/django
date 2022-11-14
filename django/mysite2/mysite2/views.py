from django.http import HttpResponse
from django.shortcuts import render


def page_view(request):
    return render(request, 'index.html')


def page2_view(request):
    return render(request, 'page2.html')


def page1_view(request, n):
    html = '这是第 %s 个页面' % n
    return HttpResponse(html)


def shebao_view(request):
    if request.method == 'GET':
        return render(request, 'calculate.html')
    elif request.method == 'POST':
        base = float(request.POST.get('base','0'))
        is_city = request.POST.get('is_city',1)
        yl_gr = base * 0.08
        yl_dw = base * 0.19
        sy_dw = base * 0.008
        if is_city == '1':
            sy_gr = base * 0.002
        else:
            sy__gr = 0
        # ...此处省略
        return render(request,'calculate.html',locals())