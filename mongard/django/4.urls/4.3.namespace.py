"""
باعث میشه که نام لینک های هر اپ از هم جدا بشن
تا مشکل تکراری بودن نام پیدا نکنیم
"""

# 1
# open './config/urls.py' and add namespace
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    '...'
    path('.../', include(('[app_name].urls', 'app_name'), namespace='[app_namespace]')),
]


# 2
# open './[app]/urls.py' and write bellow code
from django.urls import path
from . import views


app_name = '[app_namespace]'  # **********
urlpatterns = [
	path('...', 'view def or class', name='[path_name]'),
]


# 3.1
# in reverse:

"""
reverse('[app_namespace]:[path_name]', ...)
"""

# 3.2
# in html:
"""
{% url '[app_namespace]:[path_name]' %}
"""
