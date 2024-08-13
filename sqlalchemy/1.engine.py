"""
- engine
    - یه اینترفیسه برای کانکشن دیتابیس
- asynce
    - اینچیزا هم داره

"""
from sqlalchemy import create_engine


SQLALCHEMY_DATABASE_URL = ""

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # سایز پول
    # تعداد کانکشن‌های داخل پول
    pool_size=10,
    # اگه پرشد پول چندتا کانکشن بهش اضافه بشه؟
    max_overflow=30,
    # پول هرچندوقت یه بار دوباره ساخته بشه
    pool_recycle=3600,
    # تایم‌اوت پول
    pool_timeout=10,
    # pool_pre_ping=True,
)
