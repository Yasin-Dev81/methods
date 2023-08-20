# authentication
# مدیریت اکانت ها
# ex templates in "11.templates" file

# 1
# ساخت یه اپ جدید
"python manage.py startapp accounts"

# 2
# ارجاع دادن اپ به تنظیمات جنگو
# .\config\settings.py ------> INSTALLED_APPS = [..., 'accounts',]

# 3
# اضافه کردن پث اپ به فایل زیر
# .\config\urls.py
# path: path('accounts/', include('django.contrib.auth.urls')),
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # for login and logout
    path('accounts/', include('accounts.urls')), # for sign up
]


# ***
# url-path of accounts
"./venv/Lib/site-packages/django/contrib/auth/urls.py"


# 4
# ساخت فایل زیر
".\templates\registration\login.html"
# داستان تمپلیت فراموش نشه

# 5
# بازکردن دوباره فایل زیر و اضافه کردن کد زیرتر به آخر آن
".\config\settings.py"

# برای ریدایرکت یا انتقال از صفحه لاگین به لینک مورد نظر
LOGIN_REDIRECT_URL = '[url-name]' # for login
LOGOUT_REDIRECT_URL = '[url-name]' # for logout



# ***
# جنگو یوزر را به همه تمپلیت ها ارسال می کند و ما می توانیم برحسب نیاز استفاده کنیم
""" # مثال
<div class="mx-2 text-white">
    {% if user.is_authenticated %}
        Welcome {{ user }}
    {% else %}
        <a class="text-light" href="{% url 'login' %}">login</a>
    {% endif %} 
</div>
""" 

# ---------------------------------------------------------------------------------------
""" صرفا sign up """
# 0
# ساخت فایل زیر
".\templates\registration\signup.html"
# داستان تمپلیت فراموش نشه

# 1
# چک می کنیم که فایل زیر به صورت ذکر شده باشد
# .\config\urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # for login and logout
    path('accounts/', include('accounts.urls')), # for sign up
]

# 2
# ساخت فایل زیر و اضافه کردن لینک ها
"./accounts/urls.py"


# 3
# نوشتن کد زیر در ویو 
"./accounts/signup.py"

from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration\signup.html'
    success_url = reverse_lazy('login')
