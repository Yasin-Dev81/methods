"""
- بهتر است نام اپ با نام فایل یکی باشد
    * app_name --> app_name.py

- تمام آرگومان‌ها و اکسپشن‌ها را دسته‌بندی میکنه تا بتونیم به فانکشن‌ها ،سریالایزرها و... ارسالشون بکنیم

- حالات مختلف سیگنچرها
    * Partials
        ~ زمانی استفاده میشه اطلاعات رو کامل ارسال نکنیم
        ~ قسمت دیگه اطلاعات رو با کال کردن تسک سیگنچر ارسال میکنیم
    * Immutability
        ~ زمان اجرای تسک یا سیگنچر نتیجه‌ش به یه سیگنچر دیگه ارسال بشه
        ~ result.apply_async((2, 3, ), link=other_task.signature())
        ~ میتونه نتیجه‌ش ارسال نشه
            / ارسال یه سیگنچر دیگه منوط به اجرای این تسک یا سیگنچر باشه
            / result.apply_async((2, 3, ), link=other_task.signature(immutable=True))

"""
from celery import Celery
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


result = add.signature((4, 5), countdown=10)

print(result)
# خواهیم دید که یک ریزالت برابر یک تسک است فقط ارسال نشده است

# ارسال تسک ساخته شده در سیگنچر
# result.delay(for_partials="hi")
result.apply_async({'for_partials': "hi"}, link=sub.signature((2, ))) # Immutability
