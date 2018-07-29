from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("我是主页")


def detail(request, num1,num2):
    return HttpResponse("detail-%s-%s" %(num1,num2))
