from django.shortcuts import render

from django.http import HttpResponse
from .models import Grades, Students


# Create your views here.
def index(request):
    return HttpResponse("我是主页")


def detail(request, num1, num2):
    return HttpResponse("detail-%s-%s" % (num1, num2))


def grades(request):
    # 去模版中取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模版
    return render(request, 'myApp/grades.html', {"grades": gradesList})


def students(request, num):
    grade = Grades.objects.get(pk=num)
    studentList = grade.students_set.all()
    return render(request, 'myApp/students.html', {"students": studentList})
