# Docker
# یک محیط با تنظیمات یکسان ،بدون وابستگی به سیستم عامل و تنظیمات مختلف سیستم ها


# 0
# 1.startproject.py

# 1
"pip freeze > requirements.txt"

# 2
# ساخت فایل زیر
"./Dockerfile"

# 3
# نوشتن کد زیر
"""
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
"""
# تحلیل کد بالا
"""
FROM python:3.9 # نصب ورژن پایتون

ENV PYTHONDONTWRITEBYTECODE 1 # محدود کردن قابلیت ها
ENV PYTHONUNBUFFERED 1 # محدود کردن قابلیت ها

WORKDIR /code # ساخت فولدر داکر برای ریختن کد ها در آن

COPY requirements.txt /code/ # انتقال ریکوایرمنت ها به فایل کد
RUN pip install -r requirements.txt # نصب ریکوایرمنتز

COPY . /code/ # انتقال فایل ها به فولدر مشخص شده
"""

# 4
# ساخت فایل زیر
"./.dockerignore"

# 5
# نوشتن کد زیر
# فایل هایی که نمی خواهیم به داکر منتقل شود
"""
venv/
"""

# 6
# ران کردن در ترمینال
"docker build ."

# 7
# ساخت فایل زیر
"./docker-compose.yml"

# 8
# نوشتن کد زیر
# فایل هایی که نمی خواهیم به داکر منتقل شود
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
    image: postgres:14
    environment:
      - "POSTGRES_HOST_AUTH_METHOD=trust"
"""

# 9
# ران کردن در ترمینال
"docker-compose up"


# ***
# برای اجرای هرچیز در پایتون از کامند زیر استفاده می کنیم
"docker-compose exec web python manage.py [commend]"
# ex: docker-compose exec web python manage.py createsuperuser
