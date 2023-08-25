"""
- با یک دکوریتور یک تسک میتوان تعریف کرد
- دکوریتور تسک بالاتر از بقیه دکوریتورها قرار میگیره
- اگه تسک‌ها را نامگذاری نکنیم خود سلری نام‌گذاری‌اش میکند

- کال کردن تسک‌ها
    * apply_async()
        ~ with more options
    * delay()

- more options of apply_async
    * countdown
        ~ چند ثانیه بعد از دریافت شروع به اجرا شود
    * eta
        ~ بعد از تاریخ مشخص شده شروع به اجرا شود
    * expires
        ~ تاریخ انقضا
        ~ اگه بیشتر از یه حدی شد منقضی شود
        ~ هم ثانیه میتوان تنظیم کرد و هم تاریخ

"""
# task file
from celery import Celery
from time import sleep


app = Celery("app_name", broker="amqp://guest:guest@localhost:5672")


@app.task(name="app_name.adding")
def add(a, b):
    sleep(15)
    return a + b


# call task file (with delay)
from "task file" import add


add.delay(1, 3)


# call task file (with apply_async)
from "task file" import add


add.apply_async(args=[1, 3])
