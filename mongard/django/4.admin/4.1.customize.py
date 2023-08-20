"""

"""
from django.contrib import admin 
from .models import DatabaseName


"""روش اول"""
class DatabaseNameAdmin(admin.ModelAdmin) :
    # آرگومان های نمایشی
    list_display = [
        '...'
    ] # __all__
    # وقتی سرچ میکنیم تو چه ارگومان هایی بگرده
    search_fields = [
        '...'
    ]
    # فیلدهایی که قسمت فیلتر براشون فعال میشه
    list_filter = [
        '...'
    ]
    # اساس مرتب شدن
    ordering = ['datetime_created']

    # یه فیلد رو بر اساس فیلد های دیگه پرمیکنه
    prepopulated_fields = {
        'arg_1': ['arg_2', ]
    }
    # چه فیلد فارن کی ای رو براساس آیدی بهت نشون بده
    raw_id_fields = [
        'user'
    ]


admin.site.register(DatabaseName, DatabaseNameAdmin)


"""روش دوم"""
@admin.register(DatabaseName)
class DatabaseNameAdmin(admin.ModelAdmin):
    list_display = [
        '...'
    ]
    search_fields = [
        '...'
    ]
    list_filter = ['datetime_created']
    ordering = ['datetime_created']

    prepopulated_fields = {
        'arg_1': ['arg_2', ]
    }
    raw_id_fields = [
        'user'
    ]
