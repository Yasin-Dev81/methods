"""
- آدرس دهی تسک‌ها به صف موردنظر
    * وقتی به صف سلری اسم ندیم سلری اون رو به اسم سلری میذاره
    * روش خودکار سلری
        ~ واسه عوض کردنش یه فایل میسازیم و در اپ اصلی به اون ارجاع میدیم
        ~ و صف‌های موردنظر نیز باید ساخته شوند
    * روش دستی با کمبو
        ~ پکیچش با سلری نصب میشه
        ~
    * with apply_async
        ~ x.apply_async(args=(...), queue='...')

- نحوه‌ی ران کردن با ساختن صف‌های لازم واسه روش خودکار
celery -A file_name -l info -Q first,second,...
- -Q first,second,...
    - فاصله نذارین...

- واسه روش دستی نیاز نیست در کامند صفی بسازیم

- واسه دیباگ از سیگنال استفاده کن تا بفهمی که تسک به صف موردنظر رفته یا نه

"""
"in (file_name.py)"
from celery import Celery
from time import sleep


app = Celery("app_name", broker="amqp://guest:guest@localhost:5672", backend="rpc://")

# چسباندن سلری بیت به اپ
app.config_from_object('conf_file')

##### روش خودکار #####
"in (conf_file.py)"
task_default_queue = 'mongrad'

# مشخص کردن صف هر تسک
task_routes = {
    'one.add': {'queue': 'first'},
    'one.sub': {'queue': 'second'}
}

##### روش دستی با کمبو #####
"in (conf_file.py)"
from kombu import Queue, Exchange


default_exchange = Exchange('default', type='direct')
media_exchange = Exchange('media', type='direct')

task_queues = (
    Queue('default', default_exchange, routing_key='default'),
    Queue('video', media_exchange, routing_key='video'),
    Queue('image', media_exchange, routing_key='image')
)

# تنظیم صف و اکسچنج دیفالت سلری
task_default_queue = 'default'
task_default_exchange = 'default'
task_default_routing_key = 'default'

# مشخص کردن صف هر تسک
task_routes = {
    'one.add': {'queue': 'first'},
    'one.sub': {'queue': 'second'}
}
