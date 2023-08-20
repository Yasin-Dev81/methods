"""
طریقه اضافه کردن مادل به پنل ادمین

"""

# 0
# open "./app_name/admin.py" and write bellow code
from django.contrib import admin 
from .models import ModelName


admin.site.register(ModelName)
