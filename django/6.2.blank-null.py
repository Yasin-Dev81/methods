
# برای اختیاری بودن یا نبودن فیلد در دیتابیس

# black ~ ""
# null ~ None

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
    # می تواند به صورت "" و 
    # None
    # ذخیره شود.
    city = models.CharField(max_length=50, blank=True, null=False)
    # می تواند به صورت  
    # None
    # ذخیره شود.
    def __str__(self):
        return "%s with %s years old" % (self.username, self.age)

# *
# بهتر است برای 
# CharField
# فقط 
blank=True
null=False
# باشد

