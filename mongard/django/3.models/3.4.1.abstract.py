"""
- وقتی چند فیلد تکراری داشته باشیم از این قابلیت استفاده میکنیم تا کد کمتری بنویسیم
"""
# ex
from django.db import models


class Common(models.Model):
    name = models.CharField(max_lenght=30)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Student(Common):
    year = models.PositiveIntegerField()

class Teacher(Common):
    major = models.CharField(max_length=30)

