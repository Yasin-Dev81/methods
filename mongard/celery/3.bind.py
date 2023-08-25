"""
- Bound Tasks
    * تسک‌هایی که گره خوردن به خودشون
    * نحوه‌ی ساخت آن
        ~ bind=True

- retry
    * اجرای دوباره‌ی تسک
    * انواع تنظیم تایم آن
        ~ default_retry_delay
            / در حالت عادی
        ~ countdown
            / وقتی خودمان دستور میدهیم

"""
from celery import Celery


app = Celery("app_name", broker="amqp://guest:guest@localhost:5672")


@app.task(bind=True, default_retry_delay=30*60)
def add(self, a, b):
    print(self.request)
    try:
        return a / b
    except ZeroDivisionError:
        print("--- sorry!")
        self.retry(countdown=60, max_retries=5)
