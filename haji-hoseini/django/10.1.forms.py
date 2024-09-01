# مثال فرم: گرفتن یوزر و پسورد

# 0 (in html)
# پیشنیاز ها :
# csrf: cross-site request forgery
# --> یک نوع هک است که در فرم ها اتفاق می افتد
# روش جلوگیری از آن :
"""<form method="POST"> {% csrf_token %} </form>"""

# 1 (in python)
# get data of form in .views.py
# فایل زیر را باز می کنیم
"""[app-name]/views.py"""

# 2
from django.shortcuts import redirect, render

def response_def(request):
    print('method:', request.method)
    if request.method=='POST':
        print(request.POST) 
        print('title:', request.POST.get('title'))
    elif request.method=='GET':
        print(request.GET)  
    return render(request, "appname\index.html")


# **
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import DatabaseName

def add_blog_response(request):
    print('method:', request.method)
    if request.method == 'POST':
        # گرفتن اطلاعات صفحه
        print('title:', blog_title := request.POST.get('title'))
        print('text:', blog_text := request.POST.get('text'))
        user = User.objects.all()[0]
        # اضافه کردن اطلاعات به دیتابیس
        DatabaseName.objects.create(title=blog_title, text=blog_text, author=user, status='pub')
    else:
        print(request.method)
    return render(request, 'blog/add_blog.html')


