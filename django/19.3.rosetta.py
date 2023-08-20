

# 0
# installation
"docker-compose exec web pip install django-rosetta"

# 1
# open "./config/settings.py" and add app
INSTALLED_APPS = [
    # third party
    'rosetta',
]


LANGUAGE_CODE = 'fa'

LANGUAGES = (
    ('eng', 'English'),
    ('fa', 'Persian'),
)

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True

USE_L10N = True

# 2
# open "./config/urls.py" and add bellow code
urlpatterns = [
    # rosetta(i18n)
    path('rosetta/', include('rosetta.urls')),
]

# 3
# http://127.0.0.1:8000/rosetta/files/third-party/
# بازکردن لینک بالا و اضافه کردن ترجمه های لازم
