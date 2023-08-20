"""
- آرگومان‌های مفید:
    * unique : اطلاعات منحصربه‌فرد سیو بشه
    * blank : بشه بدون دیتا ثبت کرد
    * null : بشه خالی وارد کرد
"""
from django.db import models

class DBFields(models.Model):
    
    x001 = models.CharField(
        max_length=150,
        unique=True,
    )

    d = models.ForeignKey