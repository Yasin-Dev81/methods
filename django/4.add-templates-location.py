# اضافه کردن فولدر دلخواه تمپلیتمان به جنگو

# 1
# باز کردن فایل پایتون زیر در بین فایل های کانفیگ
# .\config\settings.py

# 2
# اضافه کردن پث اپ به فایل
# in 'DIRS'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(BASE_DIR.joinpath('templates-name')),# <----------------
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