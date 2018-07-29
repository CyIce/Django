from django.db import models


# Create your models here.

# 班级类
class Grades(models.Model):
    # 班级名称
    gName = models.CharField(max_length=20)
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


# 学生类
class Students(models.Model):
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
