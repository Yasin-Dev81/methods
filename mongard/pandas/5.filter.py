"""

- methods:
    - eq: ==
    - ne: !=
    - le: <=
    - lt: <
    - ge: >=
    - gt: >
    - between

- null method:
    - isnull
    - notnull

"""
import pandas as pd
import numpy as np


ep = pd.read_csv(
    "./files/employees.csv",
    parse_dates=["Start Date"]
)
ep["Mgmt"] = ep["Mgmt"].astype(bool)


## usal filter
print(ep[ep["First Name"] == "Maria"])

ep[ep["Team"]!="Finance"]

ep[ep["Mgmt"]==True]

## and filter
is_femail = ep["Gender"] == "Femail"
is_fin = ep["Team"] == "Finance"

ep[is_femail & is_fin]

## or filter
ep[is_femail | is_fin]

## not filter
ep[~is_femail]

## use methods
ep[ep.eq("Finance")]


## isin filter
# in
ep[ep["Team"].isin(["Finance", "Marketing"])]

## null methods
# اونایی که توش نال داره
ep[ep["Team"].isnull()]

# اونایی که توش نال نداره
ep[ep["Team"].notnull()]


## حذف نال‌ها از دیتا
# هر ردیفی که توش نال داشته باشه حذف میشه
ep.dropna(how="any")

# اگه همه ستون‌هاش نال باشه حذفشون میکنه
ep.dropna(how="all")

# در ستون‌های مشخص میگرده
ep.dropna(subset=["Finance", "Marketing"])

# حداقل مقادیری که نال نباشه
# حداقل 4تاش نباید نال باشه
ep.dropna(thresh=4)

## تکراری‌ها
# حذف تکراری‌ها
# keep: کدومش رو برگردونه
ep[~ep["First Name"].duplicated(keep="last")]

# برگرداندن تکراری‌ها
ep[ep["First Name"].duplicated()]

## drop duplicate
# اگه همه‌ی مقادیر تکراری بودن حذفشون کن
ep.drop_duplicates()

# تکراری‌های ستون مشخص رو حذف کن
ep.drop_duplicates(subset=["Team"], keep="last")

# اگه تکراری بودن کلا حذفشون کن (یونیک نمیشه)
ep.drop_duplicates(subset=["Team"], keep=False)
