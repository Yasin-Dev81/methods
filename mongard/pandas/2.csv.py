"""
- خوندن فایل csv

"""
import pandas as pd
import numpy as np


## گرفتن دیتا بصورت series
# return a series
pokemon = pd.read_csv(
    "./files/pokemon.csv",
    # تعیین ایندکس (ستون مشخص شده را بعنوان ایندکس میاورد)
    index_col="Pokemon"
).squeeze("columns") # تبدیل ستون باقیمونده به series

print(pokemon)

google = pd.read_csv(
    "./files/google_stocks.csv",
    # تنظیم ستون‌هایی که باید تایپ آن را تاریخ شناسایی کند
    parse_dates=["Date"],
    # چه ستون‌هایی خونده بشه؟
    usecols=["Date", "Close"],

    index_col="Date"
).squeeze()
print(google)

# sort
print(
    google.sort_values(
        ascending=False,
        na_position="first"
    )
)

# drop na
# حذف na
print(
    pokemon.dropna()
)

# sort index
# مرتب کردن براساس ایندکس‌ها
print(
    pokemon.sort_index(
        # ascending=True (default)
    )
)

# largest & smallest
# بزرگترین‌ها و کوچکترین‌ها
print(
    google.nlargest(n=3),
    google.nsmallest(n=4),
    sep="\n"
)

# تعداد هر دیتا
print(
    pokemon.value_counts(),
    pokemon.value_counts(normalize=True) # نسبت تعداد هر دیتا
)

# تعداد هر محدوده‌ی مشخص شده
bins = [0, 200, 400, 600, 1000, 1300]
print(
    google.value_counts(bins=bins)
)

# برای ایندکس‌ها
print(pokemon.index.value_counts())

# تعداد ایتم یونیک
print("nunique: ", pokemon.nunique())

# round
print("round 2:", google.round(2))


### apply
# like map
# یه فانکشن میگیره و همه‌ی ایتم‌ها رو طبق اون تغییر میده
print("apply:", google.apply(round))
