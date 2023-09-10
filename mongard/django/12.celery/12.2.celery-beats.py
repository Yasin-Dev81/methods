"""
- برنامه زمانبندی تسک‌هاست که به ما اجازه میده زمانبندیشون بکنیم
- مثلا هفته‌ای یه بار اجرا بشه

- بخش‌هایی که به پنل ادمین اضافه میشه
    * solar events
        ~ زمانبندی رو براساس طول و عرض جغرافیایی تعیین بشه
    * periodic tasks
        ~ ساخت تسک
    * intervals
        ~ تکرار یه کار خاص
    * crontabs
        ~ مانند کرون‌تب لینوکسه
    * clocked
        ~ ساخت یه زمان خاص

- روش کار
    * وارد پنل شده و زمانبندی مناسب رو میسازیم
        ~ solar events, intervals, crontabs, clocked
    * در پنل تسک مورد نظر رو هم میسازیم
        ~ periodic tasks

"""
# 0
"pip install django-celery-beat"

# 1
# open and edit "./config/settings.py"
INSTALLED_APPS = [
    '...',

    # Third-party apps
    'django_celery_beat'
]

# 2
"python manage.py migrate"

# 3
# create "./<app-name>/tasks.py" and write a task func
from celery import shared_task


@shared_task
def my_task():
    pass

# 4
# ساخت ورکر جدا برای آن
# معمولا دوتا ورکر میسازیم یکی برای سلری و یکی برای سلری بیت
"celery -A config worker -l INFO"
"celery -A config beat -l INFO --scheduler django_celery_beat.scheduler:DatabaseScheduler"
