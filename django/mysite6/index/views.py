from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index_view(request):
    return render(request,'index/index.html',locals())


def test_view(request):
    print('test被调用')
    return HttpResponse("请求到达了/test页面")


from django.conf import settings
import os
def upload_view(request):
    if request.method == 'GET':
        return render(request,'index/upload.html')
    elif request.method == 'POST':
        a_file = request.FILES["myfile"]
        print("收到上传的文件:",a_file.name)
        # 计算机保存文件的位置
        filename = os.path.join(settings.MEDIA_ROOT,a_file.name)
        with open(filename,'wb') as fw:
            fw.write(a_file.file.read())
            return HttpResponse("收到文件" + a_file.name)
        return HttpResponse("文件上传失败")

