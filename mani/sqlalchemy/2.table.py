"""

"""
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey, insert, types
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint

from typing import NewType
from datetime import UTC, datetime


# ساخت تایپ کاستوم
String50 = NewType("String50", str)


# یه بیس داره که همیشه باید خودمون بسازیمش
# برای ارثبری‌ها استفاده میکنه
class Base(DeclarativeBase):
    # تعریف تایپ‌های جدید
    type_annotation_map = {
        String50: types.String(length=50),
        # ساخت با تایم زون
        datetime: types.DateTime(timezone=True),
    }


class User(Base):
    __tablename__ = "Users"
    __table_args__ = (PrimaryKeyConstraint("id", name="user_pk"),)


    id: Mapped[types.INT]# = mapped_column(primary_key=True)
    # ستون: تایپ = ...
    # وقتی mapped_column رو میذاریم که بخوایم چیز اضافه‌ای تعریف کنیم
    username: Mapped[String50]
    email: Mapped[str | None]
    password: Mapped[str]

    # ساخت بدون تایم زون
    # این اولویت داره بر تایپ بیس
    created_at: Mapped[datetime] = mapped_column(types.DateTime(timezone=False))


class Book(Base):
    __tablename__ = "Books"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="book_pk"),
        ForeignKeyConstraint(["author_id"], ["User.id"], ondelete="CASCADE"),
    )

    id: Mapped[int]# = mapped_column(primary_key=True)

    # explicit relationship
    author_id: Mapped[types.INT]# = mapped_column(ForeignKey("Users.id"))
    title: Mapped[String50]
    created_at: Mapped[datetime]
