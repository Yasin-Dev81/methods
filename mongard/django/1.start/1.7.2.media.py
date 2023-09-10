"""
- settings of media

"""
# 0
# open "./config/settings.py" and edit this
# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 1
# فقط وقتیه که میخوایم پروژه رو توسعه بدیم استفاده بشه
# موقع اتمام توسعه باید حذف بشه
# open "./config/urls.py" and add this url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    "..."
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
