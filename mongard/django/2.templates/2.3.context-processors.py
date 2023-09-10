"""
- اگه بخواهیم یه قابلیت در تمامی صفحات در دسترس باشد
- مانند سبد خرید

- هرجا خواستیم میتونیم ذخیره‌ش کنیم ولی تو ستینگز باید بهش اشاره کنیم

"""
# 0
# create "./<app-name>/context_processors.py" and write code

def cart(request):
	return {'cart': Cart(request)}

# 1
# open "./config/settings.py" and edit this
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

				# local context-processors
                '<app-name>.context_processors.<cart>',
            ],
        },
    },
]
