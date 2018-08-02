from django.shortcuts import render

from django.http import HttpResponse
from .models import Grades, Students
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import logout
import os
from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, "myApp/index.html")


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
    # gradesList = Grades.objects.filter(students__sContend__contains="李白")

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


def attribute(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attribute")


# 获取get传递的数据，一个键带一个值
def get1(request):
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = request.GET.get("c")

    return HttpResponse(a + "   " + b + "   " + c)


# 获取get传递的数据，一个键带多个值
def get2(request):
    a = request.GET.getlist("a")
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get("c")
    return HttpResponse(a1 + "  " + a2 + "  " + c)


# POST
def registerpage(request):
    return render(request, "myApp/register.html")


def register(request):
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hobby = request.POST.getlist("hobby")
    hobby0 = hobby[0]
    # hobby1=hobby[1]
    return HttpResponse(hobby0)


# Cookie的使用
def cookie(request):
    res = HttpResponse()
    ck = request.COOKIES
    res.write("<h1>" + ck["cyice"] + "</h1>")
    res.set_cookie("cyice", "good")

    return res


# 重定向
def redirect1(request):
    return redirect("/cyice/redirect2/")


def redirect2(request):
    return HttpResponse("我是重定向后的网页")


# 登录
def main(request):
    username = request.session.get("username", "游客")

    return render(request, "myApp/main.html", {"username": username})


def login(request):
    return render(request, "myApp/login.html")


def quit(request):
    logout(request)
    return redirect("/cyice/main/")


def showmain(request):
    username = request.POST.get("username")
    # 储存session
    request.session["username"] = username
    # 设置有效时间，单位为秒，0表示关闭浏览器时失效，none表示永不过期
    request.session.set_expiry(1800)
    return redirect("/cyice/main/")


# 反向解析
def good(request):
    return render(request, "myApp/good.html")


# 模版继承
def base(request):
    return render(request, "myApp/testbase.html")


def postfile(request):
    return render(request, "myApp/postfile.html")


def showinfo(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    return render(request, "myApp/showinfo.html", {"username": username, "password": password})


# 上传文件
def upload(request):
    return render(request, "myApp/upload.html")


def savefile(request):
    if request.method == "POST":
        f = request.FILES["file"]
        filepath = os.path.join(settings.MDEIA_ROOT, f.name)
        with open(filepath, "wb") as fp:
            for info in f.chunks():
                fp.write(info)

        return HttpResponse("上传成功")

    else:
        return HttpResponse("上传失败")


def studentpage(request, page):
    allstudent = Students.objects.all()
    paginator = Paginator(allstudent, 3)
    currentlist = paginator.page(page)

    return render(request, "myApp/studentpage.html", {"students": currentlist})


# Ajax
def ajax(request):
    return render(request, "myApp/ajax.html")


def getJson(request):
    s = Students.objects.all()
    l = []
    for stu in s:
        l.append([stu.sName, stu.sAge])
    return JsonResponse({"data": l})


# 富文本
def edit(request):
    return render(request, "myApp/edit.html")
