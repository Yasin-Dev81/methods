# DatabaseName.object.filter(...) == DatabaseName.[custome-manager-name]

# 0
# open "[appname]/models.py"

# 1
# write bellow code
from django.db import models


class CustomManagerName(models.Manager):
    def get_queryset(self):
        return super(CustomManagerName, self).get_queryset().filter("...")


class Comment(models.Model):
    "..."

    # manager
    object = models.Manager()
    custom_manger_name_manager = CustomManagerName()

    "..."

