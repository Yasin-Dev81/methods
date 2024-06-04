"""
- هرچه تایپ‌های هرستون مشخص‌تر باشد مموری کمتری مصرف میشود

- category
    - کتگوری
    - تایپ دیتایی که از مقادیر خاص تشکیل شده‌اند
    - مث مرد و زن

"""
import pandas as pd
import numpy as np


ep = pd.read_csv(
    "./files/employees.csv",
    parse_dates=["Start Date"],
    usecols=["Start Date", "Mgmt", "Salary", "Gender", "Team"],
    ## method 1
    dtype={
        "Gender": "category",
        "Team": "category"
    },
    # تنظیم تعداد ردیف ایمپورت شده
    chunksize=200
)


## method 2
# عوض کردن تایپ ستون
ep["Mgmt"] = ep["Mgmt"].astype(bool)

# مقادیر خالی را صفر میگذاریم تا بشه تایپ ستون رو ست کرد
ep["Salary"] = ep["Salary"].fillna(0).astype(np.int32)


# تنظیم کتگوری
# ep["Gender"] = ep["Gender"].astype("category")
# ep["Team"] = ep["Team"].astype("category")


ep.info()
