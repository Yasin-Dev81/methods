# Static files (CSS, JavaScript, Images)

# static files: فایل هایی که ما در سرور قرار میدهیم
# media files: فایل هایی که کاربر در سرور قرار می دهد


# 1
# ساخت فولدر زیر و انتقال فایل ها به فولدر زیر
"""./static"""

# 2
# open "settings.py" and Delete this
STATIC_URL = 'static/'
# کد زیر را جایگزین بالایی می کنیم
# static files config
STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static/'))]


# 3
# in html
# "{% static '[path]' %}"

"""
{% load static %}

...

# ex:
<link rel="stylesheet" href="{% static 'css/style.css' %}">

"""
