"""
- حالت‌های مختلفی که از سیگنچرها میتونیم استفاده کنیم
- انواع آن
    * chains
        ~ تسک‌ها رو بصورت زنجیره‌وار به هم متصل میکنیم
        ~ نتیجه‌ی اولی را به دومی و دومی را به سومی و... ارسال میکند
    * groups
        ~ وقتی که بخوایم تسک‌ها رو بصورت پارالل اجرا کنیم
        ~ یه گروه تسک رو باهم ارسال کنیم
    * chords
        ~ همه‌ی تسک‌ها رو ارسال میکنه و وقتی همه‌شون درست اجرا شدن یه تسک به عنوان کال‌بک ارسال میکنه
        ~ وقتی بک‌اند دیتابیس بود میشد ازش استفاده کرد
            / با بک‌اند ربیت‌ام‌کیو کار نمیکنه

"""
from celery import Celery, chain, group, chord
from time import sleep


app = Celery("app_name", broker="amqp://guest:guest@localhost:5672")


@app.task(name="app_name.adding")
def add(a, b, for_partials):
    print(for_partials)
    sleep(15)
    return a + b

@app.task
def sub(a, b):
    return a - b

@app.task
def pp(v):
    print(v)
    return v

"chains"
result = chain(add.delay(1, 3), add.delay(6), pp.delay())
# دیدن نتیجه
print(result().get())
# دیدن نتیجه‌ی دومی
print(result().parent.get())
# دیدن نتیجه‌ی اولی
print(result().parent.parent.get())

"groups"
r2 = group(add.delay(1, 3), add.delay(6, 3), pp.delay(2))
# دیدن نتیجه
print(r2().get())
print(r2.completed_count())

"chords"
r3 = chord(add.delay(1, 3), add.delay(6, 3))(pp.delay(2))
# دیدن نتیجه
print(r3().get())

