# DecimalField
# در دیتابیس برای قیمت ها بکار میرود

max_digits=6 # ماکزیمم تعداد ارقام 
decimal_places=2 # ماکزیمم تعداد اعشار

# ex:
from django.db import models


class Book(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)

