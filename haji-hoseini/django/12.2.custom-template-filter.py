

# 0
# ساخت فایل زیر
"""appname/templatetags/__init__.py"""

# 1
# ساخت فایل فیلتر مورد نظر
"""appname/templatetags/[appname]_tags.py"""

# 2
# نوشتن کد زیر
from django import template

register = template.Library()


@register.filter
def template_filter_name1(value):
    pass # هرچی


@register.filter
def template_filter_name2(value1, value2):
    pass # هرچی



# 3
# in html
"""
{% load [appname]_tags %}


{{ value | template_filter_name1 }}

{{ value1 | template_filter_name2:value2 }}

"""
