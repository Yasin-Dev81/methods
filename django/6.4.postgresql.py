

# 0
# نصب پکیج های زیر
# روش اول
"pip install psycopg2-binary"
"pip freeze > requirements.txt"
"docker-compose up --build"
# روش دوم
"docker-compose up"
# حتما بالایی به صورت موازی ران باشد
"docker-compose exec web pip install psycopg2-binary"
"docker-compose exec web pip freeze > requirements.txt"


# 1
# open "./docker-compose.yml" and write below code:
"""
version: '3.9'

services:
  web:
    build: .
    command: python /code/manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - 8000:8000
  db:
    image: postgres:[postgres-version(leatest)]
    environment:
      - "POSTGRES_HOST_AUTH_METHOD=trust"
"""

# 2
# open "./config/settings.py" and edit below code:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# 3
# run below commend
"docker-compose up"
# حتما بالایی به صورت موازی ران باشد
"docker-compose exec web python manage.py migrate"
"docker-compose exec web python manage.py createsuperuser"
