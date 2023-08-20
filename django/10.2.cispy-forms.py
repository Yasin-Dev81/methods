# cispy forms
# اپی حاوی تمپلیت آماده برای فرم ها

# 0
"""pip install django-crispy-forms"""

# 1
# add 'crispy_forms' to (INSTALLED_APPS) in "./config/settings.py"
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party
    'crispy_forms',
]

# 2
# write (CRISPY_TEMPLATE_PACK) in "./config/settings.py"
# crispy forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# 3
# load in html file
"""{% load crispy_forms_tags %}"""

# 4
# use
"""{{ form|crispy }}"""
