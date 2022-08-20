# view 47

# 1
# ساخت سوپریوزر با دستور زیر
"""python manage.py createsuperuser"""
"""
    Username (leave blank to use 'eayea'): [username]
    Email address: [email-address]
    Password: [pass]
    Password (again): [pass] 
    Superuser created successfully.
"""

# 2
# بازکردن فایل زیر
# ./[app-name]/admin.py

# 3
# اضافه کردن مودل (دیتابیس) به فایل
from django.contrib import admin 
from .models import DatabaseName


"""روش اول"""
class DatabaseNameAdmin(admin.ModelAdmin) :
    # شخصی سازی پنل ادمین برای نمایش دیتا ها
    list_display = ['sotoon_name1', 'sotoon_name2']
    list_filter = ['datetime_created']
    ordering = ['datetime_created']


admin.site.register(DatabaseName, DatabaseNameAdmin)


"""روش دوم"""
@admin.register(DatabaseName)
class DatabaseNameAdmin(admin.ModelAdmin) :
    # شخصی سازی پنل ادمین برای نمایش دیتا ها
    list_display = ['sotoon_name1', 'sotoon_name2']
    list_filter = ['datetime_created']
    ordering = ['datetime_created']
