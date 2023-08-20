# environment variables

# 0
# نصب پکیج زیر
"[docker-compose exec web] pip install 'environs[django]'"

# 1
# open "./docker-compose.yml" and write bellow code
# اگر در سیکرت کی علامت $ بود آنرا تبدیل به دو تا می کنیم
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
    depends_on:
      - db
    environment:
      - "DJANGO_SECRET_KEY=[SECRET_KEY from settings]"
  db:
    image: postgres:14
    environment:
      - "POSTGRES_HOST_AUTH_METHOD=trust"
"""

# 2
# open "./config/settings.py" and write bellow code
from pathlib import Path
from environs import Env

# for environment variable
env = Env()
env.read_env()

"..."

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

