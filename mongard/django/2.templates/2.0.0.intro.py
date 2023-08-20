"""
- templates syntax:
    * variables
    * tags
    * filters
    * comments

- نحوه ذخیره‌سازی تمپلیت‌ها:
    * ./templates/app_name/index.html
        ~ داخل دایرکتوری مستقل تمپلیت‌ها
        ~ پیشنیاز داره000
    * ./app_name/templates/app_name/index.html
        ~ داخل هر اپ

"""

# 000
# پیشنیاز
# 0
# open "./config/settings.py" and edit bellow code
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(BASE_DIR.joinpath('templates')) # <---------------------
        ],
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
