from django.db import models
from tinymce.models import HTMLField


# Create your models here.

# 班级类
class Grades(models.Model):
    # 班级名称
    gName = models.CharField(max_length=20, unique=True)
    # 创建时间
    gDate = models.DateTimeField()
    # 总人数
    gTotalNum = models.IntegerField()
    # 女生人数
    gGirlNum = models.IntegerField()
    # 男生人数
    gBoyNum = models.IntegerField()
    # 是否被删除
    gIsDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gName

    class Meta:
        db_table = "grades"
        ordering = ["id"]


# 自定义查询集类
class StudentsManager(models.Manager):

    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(sIsDelete=False)


# 学生类
class Students(models.Model):
    # 原始查询集
    objects = models.Manager()
    # 自定义查询集,会覆盖系统自定义的查询集合
    stuObj = StudentsManager()

    # 学生名字
    sName = models.CharField(max_length=20)
    # 性别
    sGender = models.BooleanField()
    # 年龄
    sAge = models.IntegerField()
    # 个人介绍
    sContend = models.CharField(max_length=20)
    # 是否被删除
    sIsDelete = models.BooleanField(default=False)
    # 所属班级（外键）
    sGrade = models.ForeignKey("Grades", on_delete=models.CASCADE, )

    def __str__(self):
        return self.sName

    # 类方法，创建对象
    @classmethod
    def createStudent(cls, name, age, gender, content, grade):
        student = cls(sName=name, sAge=age, sGender=gender, sContend=content, sGrade=grade)
        return student

    class Meta:
        # 定义表名
        db_table = "students"
        # 排序状态 -表示降序
        ordering = ["id"]


class Text(models.Model):
    str = HTMLField()
