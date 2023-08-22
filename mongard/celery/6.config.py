"""
- معمولا برای کارهای عادی کانفیگ نمیکنیم
- ولی برای حالت پروداکشن این کار را میکنیم
- روش‌های کانفیگ کردن
    * app.conf.task_serializer = 'json'
    * app.conf.update(...)
    * app.config_from_object('<file-path>')
        ~ فایل باید پایتون باشد

- کانفیگ‌های پرکاربرد
    * task_time_limit
        ~ محدودیت برای زمان کل طول کشیده واسه تسک
    * task_soft_time_limit
        ~ محدودیت برای ران‌تایم تسک
        ~ از بالایی باید کمتر باشه
    * worker_concurrency
        ~ یه ورکر همزمان روی چندتا تسک کار کنه
    * worker_prefetch_multiplier
        ~ به هر ورکر چندتا تسک همزمان ارسال بشه؟
        ~ اگه صفر بزاریمش این کار سپرده میشه به خود ورکر
    * task_ignore_result
        ~ نتایج رو ذخیره نکنه
        ~ معمولا واسه ایمیل بکار میره
    * task_always_eager
        ~ تسک‌ها در سیستم کلاینت اجرا میشن
        ~ فقط واسه دیباگ استفاده میشه
    * task_acks_late
        ~ بعد از دریافت ریزالت تیک انجام تسک زده شود
    *

"""
from celery import Celery


app = Celery("app_name", broker="amqp://guest:guest@localhost:5672", backend='rpc://')

app.conf.update(
    task_time_limit=60,
    task_soft_time_limit=50,
    worker_concurrency=7,
    worker_prefetch_multiplier=0,
    task_ignore_result=True,
    # task_always_eager=True,
    task_acks_late=True,
)
