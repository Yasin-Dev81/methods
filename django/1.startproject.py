# config : settings of django site
# app : page of django site

# ساخت ادمین پروژه در فایل پروژه
# django-admin startproject config 
#                               -----------> config -> config -> admin
# or
# django-admin startproject config . 
#                               ---------> config -> admin
# config : فایلی حاوی تنظیمات پروژه


# ران کردن سرور
# python manage.py runserver


# ساخت اپ برای جنگو
# python manage.py startapp [appname]

# ارجاع دادن اپ به تنظیمات جنگو
# روش اول
# .\config\settings.py ------> INSTALLED_APPS = [..., '[appname]',]
# روش دوم
# .\config\settings.py ------> INSTALLED_APPS = [..., '[appname].apps.[appname]Config',]
