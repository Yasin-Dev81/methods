"""
- models
    * دیتابیس رو مشخص میکنن و ساختار ذخیره‌سازی اطلاعات رو مشخص میکنن

- tables
    * جداول اطلاعات هستن
    * باید مشخص کنیم که چه اطلاعاتی باید توش ذخیره بشه

- model = table
    * به شرطی که:
        ~ class model(models.Model): > ارثبری کنه
        ~ داخلش مشخص بشه که چه فیلدهایی رو میخوایم

"""

# 0 
# open "./app_name/models.py" and write models

from django.db import models


# جمع نوشته نشه
class ModelName(models.Model):
    '...'

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


# 1
# migration
"""
python manage.py makemigrations
python manage.py migrate
"""
