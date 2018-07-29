from django.shortcuts import render

from django.http import HttpResponse
from .models import Grades, Students
from django.db.models import Max


# Create your views here.
def index(request):
    return HttpResponse("我是主页")


def detail(request, num1, num2):
    return HttpResponse("detail-%s-%s" % (num1, num2))


from django.db.models import F, Q


def grades(request):
    # 去模版中取数据
    gradesList = Grades.objects.all()

    # F对象
    # gradesList = Grades.objects.filter(gGirlNum__gt=F("gBoyNum")+5)

    # Q对象，实现或的功能，前面加一个～表示取反
    # gradesList = Grades.objects.filter(Q(pk=3) | Q(pk=2))

    # 关联查询Grades表和Students表，在查询学生表中学生名字含有'李白'的学生的班级
    gradesList = Grades.objects.filter(students__sContend__contains="李白")

    # 将数据传递给模版
    return render(request, 'myApp/grades.html', {"grades": gradesList})


def students(request, num):
    grade = Grades.objects.get(pk=num)
    studentList = grade.students_set.all()
    return render(request, 'myApp/students.html', {"students": studentList})


def studentInfo(request):
    infoList = Students.objects.all()
    # 分页
    # infoList = Students.objects.all()[1:3]

    # 外键
    # 属性名_id

    # 比较运算符
    # infoList = Students.objects.filter(sAge__gt=80)

    # 模糊查询
    # infoList = Students.objects.filter(sName__contains="李")
    # 不区分大小写
    # infoList = Students.objects.filter(sName__icontains="李")

    # 聚合函数
    # maxAge=Students.objects.aggregate(Max("sAge"))
    # print(maxAge)


    return render(request, "myApp/students.html", {"students": infoList})


def addstudent(request):
    grade = Grades.objects.get(pk=4)
    student = Students.createStudent("李贺", 71, True, "我是李贺哈哈哈", grade)
    student.save()
    return HttpResponse("创建成功")
