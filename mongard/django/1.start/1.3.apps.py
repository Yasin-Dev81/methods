"""
واسه مدیریت و توسعه راحت‌تر و سریع‌تر پروژه جنگو پروژه رو به قسمت‌های کوچک‌تر به اسم
app 
تقسیم‌بندی میکنیم



"""
# - مراحل:

# 0
# ساخت اپ
"python manage.py startapp <app_name>"

# 1
# open "./config/settings.py" and add <app_name>
INSTALLED_APPS = [
    '...',
    'app_name',
    'app_name.apps.App_nameConfig'  # روش پیشنهادی
]

# 2
# open "./config/urls.py" and add <app_name> url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('[app_name_path]/', include('[app_name].urls')),
]

# 3
# create and open "./app_name/urls.py" for add AppsUrl
from  django.urls import path
from .views import def1_view

urlpatterns = [
    path('[view_url_path]/', def1_view, name='[view_url_name]'),
]

# 4
# ساخت تابع(های) ویو
# open "./app_name/views.py"
def def1_view(request):
    pass

class Class1View:
    pass

