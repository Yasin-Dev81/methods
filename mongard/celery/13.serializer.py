"""
- سریالایز کردن
    * تبدیل اطلاعات به نوع جی‌سون
    * چون ورکرها با بروکرها اینطوری ارتباط برقرار میکنن
    * برای اینستنس‌های پیچیده مانند کلاس به مشکل میخوریم
        ~ راه‌حل
            \ به جای جی‌سون از پیکل استفاده میکنیم

"""
"in (file_name.py)"
from celery import Celery


app = Celery("app_name", broker="amqp://guest:guest@localhost:5672", backend="rpc://")

# تغییر سریالایزر
app.conf.update(
    task_serializer='pickle',
    result_serializer='pickle',
    accept_content=['application/x-python-serialize']
)


@app.task
def call(person):
    return person.show()


"in request file"

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


    def show(self):
        return f"{self.name} is {self.age} years old."


p1 = Person('yasin', 21)

r = call.delay(p1)
print(r.get())
