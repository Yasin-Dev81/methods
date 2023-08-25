"""
- تسک‌های زمانبندی شده
    * باید برای آن یه فایل دیگه به عنوان سلری بیت رو هم اجرا کنیم

- اجرای اپ اصلی
celery -A file_name -l info

- اجرای سلری بیت
celery -A conf_file beat

"""
"in (file_name.py)"
from celery import Celery, signals
from time import sleep


app = Celery("app_name", broker="amqp://guest:guest@localhost:5672", backend="rpc://")

# چسباندن سلری بیت به اپ
app.config_from_object('conf_file')

@app.task
def show(name):
    print(f"Hello {name}")


"in (conf_file.py)"
from celery.schedules import crontab


beat_schedule = {
    'chall_show_every_one_minute': {
        'task': 'app_name.show',
        'schedule': crontab(minute='*/1'),
        'args': ('yasin', )
    }
}
