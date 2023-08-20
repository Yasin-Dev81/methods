
# Rel. :
# دیتابیس های رابطه ای --> جدولی
# lang: SQL
# خود جنگو قابلیت دیتابیس های رابطه ای را برای ما فراهم کرده است.
# in sqlite


# 1
# باز کردن فایل زیر
"""./[app-name]/models.py"""

# 2
# ساخت کلاس با استایل زیر برای دیتابیس
from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class DatabaseName(models.Model) :
    sotoon_name1 = models.CharField(max_length=100, verbose_name="اسم نمایشی") # for str
    sotoon_name2 = models.DecimalField(max_digits=3) # for decimal
    sotoon_name3 = models.EmailField(max_length=30) # for email
    sotoon_name4 = models.DateField() # only date
    sotoon_name5 = models.DateTimeField(auto_now_add=True) # date + time 
    # auto_now_add: موقع ساخت اتوماتیک سیو میشود و تغییر نمی کند
    # auto_now: هر موقع که تغییری ایجاد میشودزمان زمان سیو می شود
    sotoon_name6 = models.TimeField() # only time
    sotoon_name7 = models.TextField() # بدون محدودیت
    choices_tupel = (
        ('short-name', 'name'), 
    )
    sotoon_name8 = models.CharField(choices=choices_tupel, max_length=10)

    # foreign key: ارجاع دادن به یک دیتابیس(مودل) دیگر
    # id(primary key): به صورت پیشفرض هر مدل یا دیتایی که در دیتابیس اضافه میشود یک آی دی منحصر به فرد می گیرد.
    # مدیریت یوزر ها را خود جنگو برای ما آمده کرده(قسمت یوزرز ادمین)
    # auth = authentication = اپ دیفالت جنگو برای یوزر ها
    # می خواهیم آی دی که از اپ بالا بدست آمده را اینجا زخیره کنیم
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # on_delete: اگر یوزر دیلیت شد چه اتفاقی بیوفتد
    other_forgen1 = models.ForeignKey('[ModelName]', on_delete=models.CASCADE) # تو این فایل نیست
    other_forgen2 = models.ForeignKey(ModelName, on_delete=models.CASCADE, related_name='[databasename]s') # تو این فایل هست
    # ModelName.[databasename]s.all() : همه دیتا های فارن کی

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str: # در پنل ادمین نشان میدهد
        return self.sotoon_name1

    def get_absolute_url(self):# بعد از اضافه شدن به دیتابیس به لینک قید شده ریدایرکت میشود
        return reverse('[url-name]', args=[, ])


# 3
# ساخت دیتابیس با دستور زیر
# ساخت مایگریت
"""python manage.py makemigrations [app-name]"""
"""docker-compose exec web python manage.py makemigrations [app-name]"""

# 4
# مایگریت کردن
"""python manage.py migrate"""
"""docker-compose exec web python manage.py migrate"""

# 5 
# get data from database in views
from django.shortcuts import render
from .models import DatabaseName

def response_def(request) : # all
    notes = DatabaseName.objects.all()
    return render(request, "appname\index.html")

def response_def(request, pk) : # with pk/id
    notes = DatabaseName.objects.get(pk=pk)
    return render(request, "appname\index.html")

def response_def(request) : # with filter
    notes = DatabaseName.objects.filter(sotoon_name8='short-name')
    return render(request, "appname\index.html")

def response_def(request) :
    notes = DatabaseName.objects.all().order_by('sotoon_name7') # ترتیب دادن
    notes = DatabaseName.objects.all().order_by('-sotoon_name7') # ترتیب دادن معکوس
    return render(request, "appname\index.html")

# ***
# add on database
from .mudels import DatabaseName
DatabaseName.objects.create(
    sotoon_name1=None,
    sotoon_name2=None,
    sotoon_name3=None,
    sotoon_name4=None,
    sotoon_name5=None,
    sotoon_name6=None,
    sotoon_name7=None,
    sotoon_name8=None,
    author=None,
)
