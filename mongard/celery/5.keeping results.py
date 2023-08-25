"""
- keeping results
    * ذخیره کردن پاسخ‌ها
    * انواعش
        ~ rpc://
            / rabitmq
        ~ redis://
            / ردیس

# آیا پاسخ آماده است؟
x.ready()

# گرفتن پاسخ
x.get()

# فقط نوع اکسپشن را ریترن کند و نه بیشتر
x.get(propagate=False)

# گرفتن اکسپشن
x.traceback

# دیدن وضعیت تسک
x.status
- وضعیت‌ها
    * pending, started, retry, failure, success

"""
# task file
from celery import Celery
from time import sleep


app = Celery("app_name", broker="amqp://guest:guest@localhost:5672")


@app.task(name="app_name.adding")
def add(a, b):
    sleep(15)
    return a + b

# call task file
from "task file" import add


r = add.delay(1, 3)

if r.ready():
    print(r.get())
