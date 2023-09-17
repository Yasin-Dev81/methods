FROM python:latest # دریافت ایمیج پایتون

WORKDIR /code # ساخت دایرکتوری برای کد

COPY requirements.txt /home/code/

# pip
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /code/ # کپی کردن کد پروژه تو ایمیج

EXPOSE 8000 # باز کردن پورت 8000

CMD ["gunicorn", "config.wsgi", ":8000"] # ران کردن جنگو با گنیکورن

