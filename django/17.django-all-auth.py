
# 0
"pip install django-allauth"

# 1
# open "./config/settings.py" and write bellow code

INSTALLED_APPS = [
    '...',

    'allauth',
    'allauth.account',
]

AUTHENTICATION_BACKENDS = [
    # Needed to log in by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# ACCOUNT_SESSION_REMEMBER = True

# اگر بخواهیم ایمیل اولویت بیشتری از یوزرنیم داشته باشد
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

# 2
# open "./config/urls.py" and write bellow code
urlpatterns = [
    '...',
    path('accounts/', include('allauth.urls')),
]


# 3
# تغییر نام فولدر زیر
"./templates/registration"
# به
"./templates/account"

# 4
# به فایل های زیر احتیاجی نداریم پس محتوای انها را پاک می کنیم
"./accounts/urls.py"
"./accounts/views.py"

# 5
# migrate
"[docker-compose exec web] python manage.py migrate"
