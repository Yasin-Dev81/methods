# برای داخل کد ها

# 1
# ex "views.py":
from django.utils.translation import gettext as _
from django.http import HttpResponse

def ex_view(request, pk):
    return HttpResponse(_('Access is limited'))

# ex "models.py":
from django.utils.translation import gettext_lazy as _
from django.db import models

class Comment(models.Model):
    comment_text = models.TextField(blank=False, null=False, verbose_name=_('comment'))
    "..."

# 2
# run bellow code in commend
"cd [app-name]"
"django-admin makemessages -l fa"

# 3
# نوشتن ترجمه هر متن آورده شده
# ex:
"""
#: .\templates\products\products_detail.html:178
msgid "submit"
msgstr "ارسال"
"""

# 4
# run bellow code in commend
"cd [app-name]"
"django-admin compilemessages"

# fuzzy: کلمات و جملات مشابه رو خودش پر میکنه
