"""

"""
import pandas as pd
import datetime as dt
from pandas.tseries.offsets import DateOffset


# ساخت تایم
# like datetime
pd.Timestamp(year=1991, month=4, day=12)

pd.Timestamp(ts_input="1991-04-12 8:50:45 PM")

pd.Timestamp(ts_input=dt.datetime(1991, 4, 12, 13, 34, 50))


# تبدیل ستون‌های تاریخ دیتا به دیت‌تایم
disney = pd.read_csv(
    "./files/disney.csv"
    # method 1
    # parse_dates=["Date"]
)
# method 2
disney["Date"] = pd.to_datetime(disney["Date"])


# use dt
print("years:", disney["Date"].dt.year)


# example:
# گروه‌بندی براساس روز‌های هفته
disney["WeekDay"] = disney["Date"].dt.day_name()

g = disney.groupby("WeekDay")
print("mean of week day:", g.mean(numeric_only=True))


## DateOffset
# اضافه کردن 5 روز به ستون تاریخ
disney["Date"] += DateOffset(day=5)
print(disney)

# رند کردن به ماه بعدی
disney["Date"] += pd.offsets.MonthEnd()


## TimeDelta
# ساختش
pd.Timedelta(days=5, minutes=15, hours=3)

pd.to_timedelta("3 hours, 5 minutes, 12 seconds")

# ساخت یه سیریز با تایم‌دلتا‌های مشخص
# همه براساس روز
pd.to_timedelta([5, 10, 15], unit="day")


# example
dlv = pd.read_csv(
    "./files/deliveries.csv",
    parse_dates=["order_date", "delivery_date"]
)

# ساخت ستون فاصله زمان‌ها
dlv["duration"] = dlv["delivery_date"] - dlv["order_date"]

print(dlv[dlv["duration"] > pd.Timedelta(days=365)])
