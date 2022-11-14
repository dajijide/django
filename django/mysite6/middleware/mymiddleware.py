from django.utils.deprecation import MiddlewareMixin
from django.http import Http404, HttpResponse


class MyMW(MiddlewareMixin):
    def process_request(self, request):
        print("中间件process_request方法调用")


class VisitLimit(MiddlewareMixin):
    # 此字典的建为IP地址值为，此IP地址的访问次数
    visit_times = {}

    def process_request(self, request):
        ip = request.META['REMOTE_ADDR']  # 得到客户端IP
        if request.path_info != '/test':
            return None
        # 获取以前的访问次数
        times = self.visit_times.get(ip, 0)
        print('IP', ip, '已访问过test', times, '次')
        self.visit_times[ip] = times + 1
        if times < 5:
            return None
        return HttpResponse("您已经访问过:" + str(times)+'次')
