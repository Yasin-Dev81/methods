"""
- سلری را به جنگو اضافه میکنیم تا تسک‌هایی که زمان زیادی طول میکشد را انجام دهد

"""
# 0
"pip install celery"

# 1
# create "./config/celery_conf.py" and write bellow code
from celery import Celery
from datetime import timedelta
import os


# env of django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# create celery app
# همنام پروژه باشه
celery_app = Celery('config')
# در هر اپ که فایل تسک داشته باشیم اجراش میکنه
celery_app.autodiscover_tasks()

# conf of broker (more info in celery directory)
celery_app.conf.broker_url = 'amqp://username:password@addres:port'
celery_app.conf.result_backend = 'rpc://'
celery_app.conf.task_serializer = 'json'
celery_app.conf.result_serializer = 'pickle'
celery_app.conf.accept_content = ['json', 'pickle']
celery_app.conf.result_expires = timedelta(days=1) # تاریخ انقضای تسک‌ها
# منتظر گذاشتن (بلاک کردن) کاربر تا زمانی که تسک تمام نشده
celery_app.conf.task_always_eager = False
# هر ورکر حق داره چندتا تسک همزمان انجام بده
celery_app.conf.worker_prefetch_multiplier = 4


# 2
# create "./config/__init__.py" and write bellow code
from .celery_conf import celery_app
