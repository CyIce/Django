# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 16:25
# @Author  : CyIce
# @Email   : 1207201395@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

app_name = "myApp"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:num1>/<int:num2>/', views.detail),
    path('grades/', views.grades),
    path('grades/<int:num>/', views.students),
    path('student/', views.studentInfo),
    path('addstudent/', views.addstudent),
    path('attribute/', views.attribute),
    path('get1/', views.get1),
    path('get2/', views.get2),
    path('register/', views.registerpage),
    path('register/reg/', views.register),
    path('cookie/', views.cookie),

    # 重定向
    path("redirect1/", views.redirect1),
    path("redirect2/", views.redirect2),

    # 登录
    path("main/", views.main),
    path("login/", views.login),
    path("showmain/", views.showmain),
    path("logout/", views.quit),

    # 反向解析
    path("good/", views.good, name="good"),

    # 模版继承
    path("base/",views.base)
]
