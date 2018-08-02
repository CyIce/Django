from django.contrib import admin

# Register your models here.
from .models import Grades, Students, Text


class StudentsInfo(admin.TabularInline):  # TabularInline
    model = Students
    extra = 2


@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    def isDelete(self):
        if self.gIsDelete:
            return "已删除"
        else:
            return "存在"

    isDelete.short_description = "是否删除"

    inlines = [StudentsInfo]
    # 列表属性
    list_display = ["pk", "gName", "gDate", "gTotalNum", "gGirlNum", "gBoyNum", isDelete]
    # 过滤器
    list_filter = ["gName"]
    # 搜索字段
    search_fields = ["gName"]
    # 分页
    list_per_page = 5

    # 添加、修改页面
    # fields = ["gName", "gDate", "gTotalNum", "gBoyNum", "gGirlNum", "gIsDelete"]
    # 给属性分组，不能与fields同时使用
    fieldsets = [
        ("base", {"fields": ["gName", "gDate"]}),
        ("num", {"fields": ["gTotalNum", "gGirlNum", "gBoyNum"]}),
        ("isDelete", {"fields": ["gIsDelete"]})
    ]


# 注册
# admin.site.register(Grades, GradesAdmin)


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sGender:
            return "男"
        else:
            return "女"

    def isDelete(self):
        if self.sIsDelete:
            return "已删除"
        else:
            return "存在"

    isDelete.short_description = "是否删除"
    gender.short_description = "性别"

    list_display = ["pk", "sName", "sAge", gender, "sContend", "sGrade", isDelete]
    list_per_page = 2


# admin.site.register(Students, StudentsAdmin)


admin.site.register(Text)
