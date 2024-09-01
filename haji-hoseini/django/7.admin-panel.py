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
class DatabaseNameAdmin(admin.ModelAdmin):
    # شخصی سازی پنل ادمین برای نمایش دیتا ها
    list_display = ['sotoon_name1', 'sotoon_name2']
    list_filter = ['datetime_created']
    ordering = ['datetime_created']


# Tabular Inline
# Stacked Inline
# نشان دادن فارن کی ها در ادمین
class DatabaseName2Inline(admin.TabularInline):  # TabularInline
    model = DatabaseName
    fields = ['product', 'author', 'active', 'stars', ]
    extra = 1 

class DatabaseName3Inline(admin.StackedInline):  # StackedInline
    model = DatabaseName
    fields = ['product', 'author', 'active', 'stars', ]
    extra = 1 # تعداد نمایش خالی ها

@admin.register(DatabaseName)
class DatabaseNameAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'price', 'datetime_created']
    list_filter = ['datetime_created']
    ordering = ['-datetime_created']

    inlines = [
        DatabaseName2Inline,
        DatabaseName3Inline,
    ]
