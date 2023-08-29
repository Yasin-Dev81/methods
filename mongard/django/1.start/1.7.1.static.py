"""
- settings of static

"""
# 0
"./config/settings.py"
# در اینستالد اپز باشه و

# واسه هر اپ
STATIC_URL = 'static/'

# واسه دایرکتوری اصلی
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# 1
# on html
"""
{% load static %}

{% static '<local-path>' %}
"""
