"""
محل قرارگیری فایل‌های فرانت پروژه‌س

- محل دایرکتوری‌ها:
    * ./app_name/templates/app_name/
    * ./templates/app_name/
        ~ قبل‌ش باید مراحل زیر رو برید

"""

# مراحل دایرکتوری دوم

# 0
# create "./templates/app_name/" directory

# 1
# open "./config/settings.py" and add template-directory
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]