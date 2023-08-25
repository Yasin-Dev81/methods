"""
- برای استفاده باید اول یک اینستنس (اپ) بسازیم
- چندتا اپ مختلف سلری میتونن در کنار هم با کانفیگ‌های مختلف و تسک‌های مختلف کنار همدیگه به خوبی کار بکنن و هیچ تداخلی نداشته باشن

- amqp://guest:guest@localhost:5672
    * ربیت‌ام‌کیو با رمز و پسورد

- ران کردن ورکر سلری
celery -A file_name worker

- تنظیم دریافت نوع لاگ‌ها
celery -A file_name -l info
- انواع لاگ‌ها
    * debug, info, warning, error, critical, fatal

"""
from celery import Celery

app = Celery("app_name", broker="amqp://guest:guest@localhost:5672")
