"""
- DateField args:
    * auto_now
        ~ هروقت ابجکتی سیو بشه یا تغییر کنه سیو میکنه
    * auto_now_add
        ~ وقتی اولین بار ایجاد میشه اتومات مقدار دهی میکنه

"""
from django.db import models

class ModelName(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
