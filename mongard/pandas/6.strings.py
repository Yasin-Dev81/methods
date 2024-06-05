"""

"""
import pandas as pd
import numpy as np


cg = pd.read_csv("./files/chicago_food_inspections.csv")


# حذف اسپیس‌های اضافی اول و آخر
# one column
cg["Name"] = cg["Name"].str.strip()
# حذف اسپیس‌های سمت چپ
cg["Name"] = cg["Name"].str.lstrip()
# حذف اسپیس‌های سمت راست
cg["Name"] = cg["Name"].str.rstrip()

# کوچک کردن حروف
cg["Name"] = cg["Name"].str.lower()
# بزرگ کردن حروف
cg["Name"] = cg["Name"].str.upper()
# حرف اول بزرگ باقی کوچک
cg["Name"] = cg["Name"].str.title()


# all columns
for col in cg.columns:
    cg[col] = cg[col].str.strip().str.title()

print(cg)


# ----------------------
# تمیز کردن دیتا

# remove na
cg = cg.dropna(subset=["Risk"])
# replace
cg = cg.replace(to_replace="All", value="Risk 4 (Extreme)")
# بریدن عدد ریسک
cg["Risk"] = cg["Risk"].str.slice(5, 6)
# cg["Risk"] = cg["Risk"].str[5:6]

print(cg)

# -----------------------
# شامل یه استرینگ باشن
cg[cg["Name"].str.lower().str.contains("pizza")]

# با یه استرینگ شروع بشه
cg[cg["Name"].str.lower().str.startswith("pizza")]

# با یه استرینگ تموم بشه
cg[cg["Name"].str.lower().str.endswith("pizza")]


# -------------------------
## regex
# هرجا اولش عدد بود جایگزین کن
cg["Address"].str.replace("^\d+", "*", regex=True)

# split
cg["Name"].str.split(
    pat=" ",
    # چندبار تیکه‌ش کنه
    n=1
).str.get(0) # اولین مقدار رو برمیگردونه تو اسپلیت

# تبدیل به دیتافریم
cg["Name"].str.split(
    pat=" ",
    # چندبار تیکه‌ش کنه
    n=1,
    expand=True
)


## ساخت ستون جدید از ستون‌های قبلی
cg[["First Name", "Last Name"]] = cg["Name"].str.split(" ", n=1, expand=True)

# حذف ستون قبلی
cg.drop(labels=["Name"], axis="columns")
