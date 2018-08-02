# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 10:50
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : mymiddleware.py
# @Software: PyCharm

from django.utils.deprecation import MiddlewareMixin


# 自定义中间件
class MyMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        print("Get的参数为：", request.GET.get("a"))
