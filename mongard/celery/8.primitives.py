"""
- کارهای سیگنال
    * وقتی میخواهیم بخش‌های مختلف برنامه‌مون رو از یک اتفاق مطلع کنیم
    * اتصال برنامه‌های مختلف به یکدیگر

- signals
    * before_task_publish
        ~ قبل ارسال تسک
    * after_task_publish
        ~ بعد از ارسال تسک
    * task_prerun
        ~ قبل از اجرای تسک
    * task_postrun
        ~ بعد از اجرای تسک
    * task_retry
        ~ زمانی که یه تسک ریترای بشه
    * task_seccess
        ~ زمانی که تسک موفقیت‌آمیز باشه
    * task_failure
        ~ وقتی تسک فیل میشه
    * task_internal_error
        ~ وقتی تسک به ارور داخلی سلری برخورد کنه
    * task_received
        ~ وقتی که تسک به دست بروکر میرسه
    * task_revoked
        ~ زمانی که تسک شکست بخوره یا توسط ورکر قطع بشه
    * task_unknown
        ~ زمانی که تسکی دریافت کنیم که رجیستر نشده باشه
    * task_rejected
        ~ زمانی که یه تسک به بروکر بیاد که ناشناخته باشه
    * celeryd_after_setup
        ~ بعد از ست‌آپ شدن ورکر
    * celeryd_init
        ~ زمانی که ورکر شروع به کار بکنه
    * worker_init
        ~ قبل از شروع به کار ورکر
    * worker_ready
        ~ وقتی ورکر آماده به کار باشد
    * worker_shutting_down
        ~ زمانی که ورکر میخواد خاموش بشه
    *
"""
from celery import Celery, signals
from time import sleep


app = Celery("app_name", broker="amqp://guest:guest@localhost:5672")


@app.task(name="app_name.adding")
def add(a, b, for_partials):
    print(for_partials)
    sleep(15)
    return a + b


# وقتی که به تسک به ادد ارسال میشه این تابع سیگنال دریافت میکنه
@signals.task_prerun.connect(sender=add)
def show(sender=None, **kwargs):
    print('task before run')
    print(sender)
    print(kwargs)
