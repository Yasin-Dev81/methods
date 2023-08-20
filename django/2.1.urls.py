# view : get request and send response in django site
# request --> |view| --> response


# منطق لینک ها:
# مراحل :

# 1
# باز کردن فایل پایتون زیر در بین فایل های اپ
# .\[appname]\views.py

# 2
# نوشتن متن زیر در فایل پایتون
from django.shortcuts import render
from django.http import HttpResponse

# --------> exampel -> without html
def response_def    (request) : # تابع ریسپانس با اسم دلخواه
    return HttpResponse("welcome:)") # --------> exampel

# --------> exampe2 -> with html
def response_def(request) : # تابع ریسپانس با اسم دلخواه
    return render(request, "appname\index.html")
# path of html: appname\templates\appname\index.html

# --------> exampe2 -> send variable
def response_def(request) : # تابع ریسپانس با اسم دلخواه
    context_dictionary = {
        "Variable": "somthing",
    }
    return render(request, "appname\index.html", context_dictionary)

# --------> exampe3 -> get data from database
from .models import database_name
def response_def(request) :
    notes = database_name.objects.all()
    # notes = database_name.objects.all().order_by('datetime_edited') # ترتیب دادن
    return render(request, "appname\index.html")

# --------> exampe4 -> with input
from .models import database_name
def response_def_with_input(request, input_name) :
    x = input_name
    return render(request, "appname\index.html")

# 3
# ساخت یک فایل پایتون در اپ مورد نظر 
# .\[appname]\urls.py

# 4
# نوشتن متن زیر در فایل پایتون
from  django.urls import path
from .views import response_def # تابع ریسپانس ساخته شده در مرحله 2

urlpatterns = [
    path('[url-path-1]/', response_def, name='[url-name-1]'),
    path('<int:input_name>/', response_def_with_input, name='[url-name-2]'),
]
'''
    url1 in html: href="{% url '[url-name-1]' %}"
    url2 in html: href="{% url '[url-name-2]' [input_name] %}"
'''

# 5
# باز کردن فایل پایتون زیر در بین فایل های کانفیگ
# .\config\urls.py

# 6
# اضافه کردن پث اپ به فایل
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('[url-path-2]/', include('[appname].urls')),
]

# 7
# return link: www.[site]/[url-path-2]/[url-path-1]
"""
    url-path-2: set in config
    url-path-1: set in app
"""
