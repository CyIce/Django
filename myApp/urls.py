# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 16:25
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:num1>/<int:num2>', views.detail)
]
