# static files: فایل هایی که ما در سرور قرار میدهیم
# media files: فایل هایی که کاربر در سرور قرار می دهد

"just localhost"
# 0
# install "Pillow"
"""pip install Pillow"""

# 1
# open "./config/settings.py" and write this code
# media files
MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR.joinpath('media'))

# 2
# ساخت فولدر زیر
"""./media"""

# 3
# ساخت فولدر های مورد نیاز در فولدر مدیا
"""./media/[media-name]"""
# ex: './media/covers'

# 4
# open "./config/urls.py" and add this url

# from django.contrib import admin
# from django.urls import path, include
from distutils.command.upload import upload
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    "..."
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 5
# add to models
from django.db import models

class DataBaseName(models.Model):
    '...'
    sotoon_media = models.ImageField(upload_to='[media-name]/', blank=True)
    # ex:
    cover = models.ImageField(upload_to='covers/', blank=True)
    '...'

# 6
# مایگریت کردن
"""python manage.py makemigrations [app-name]"""
"""python manage.py migrate"""

# 7
# add to html
"{{ x.[sotoon_media].url }}"
# ex:
"""
    {% if book.cover %}
        <img src="{{ book.cover.url }}">
    {% else %}
        <p>There is no photo</p>
    {% endif %}
"""

# 8
# in forms
