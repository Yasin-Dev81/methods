

# 0
"pip install psycopg2 gunicorn django-heroku whitenoise"

# 1
"pip freeze > .\requirements.txt"

# 2
# create "./Procfile" and write this code
"""
release: python manage.py migrate
web: gunicorn config.wsgi --log-file -
"""

# 3
# add bellow code to "./config/settings.py"
import django_heroku

STATIC_ROOT = str(BASE_DIR.joinpath('static'))
STATIC_URL = 'static/'
django_heroku.settings(locals())
