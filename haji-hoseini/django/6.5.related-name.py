
# in models.py:
from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class DatabaseName(models.Model) :
    other_forgen2 = models.ForeignKey(ModelName, on_delete=models.CASCADE, related_name='[databasename]s') # تو این فایل هست
    # ModelName.[databasename]s.all() : همه دیتا های فارن کی
    # ...


# in html:

"""
    {% for x in ModelName.[databasename]s.all %}

    {% endfor %}
"""
