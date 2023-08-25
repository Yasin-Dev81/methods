"""
- flower
    * رابط گرافیکی سلری

pip install flower

celery --broker=amqp://guest:guest@localhost:5672// flower

# دیدن وضعیت نودها
celery status

# حذف تمامی تسک‌ها
celery purge [-A app_name]

# دیدن تسک‌های اکتیو
celery inspect active [-A app_name]

# دیدن تسک‌های شکست خورده
celery inspect revoked [-A app_name]

# دیدن اطلاعات ورکر
celery inspect stats
"""
