"""
- pivot

- تبدیل هر ابجکت‌های هر لیست به یک ردیف مختلف
    - ds.explode(columns=["..."])

"""
import pandas as pd
import numpy as np


ds = pd.read_csv(
    "./files/sales_by_employee.csv",
    parse_dates=["Date"]
)

pivot = ds.pivot_table(
    # ستون ایندکس
    index="Date",
    # ستون‌هایی که استفاده بشه
    values=["Expenses", "Revenue"],
    # ایندکس‌های هرستون
    columns=["Name"],
    # تابعی که اجرا بشه
    aggfunc=["sum"],
    # total
    margins=True,
    margins_name="Total",
    # nan values
    fill_value=0
)
print(pivot)

pivot2 = ds.pivot_table(
    # ستون ایندکس
    index="Date",
    # ستون‌هایی که استفاده بشه
    values=["Expenses", "Revenue"],
    # ایندکس‌های هرستون
    columns=["Name"],
    # تابعی که اجرا بشه
    aggfunc={
        "Expenses": "sum",
        "Revenue": "mean"
    },
    # total
    margins=True,
    margins_name="Total",
    # nan values
    fill_value=0
)


# تبدیل دیتافریم به سریز
pivot2.stack()

pivot3 = ds.pivot_table(
    index=["Customer", "Name"],
    values="Revenue",
    aggfunc="sum"
)

# تبدیل ایندکس به ستون
pivot3.unstack()

# برعکس کننده پیوت
vg = ds = pd.read_csv("./files/video_game_sales.csv")

vg2 = pivot.melt(
    # ستونی که ایندکس بشه
    id_vars="Name",
    # ستون‌هایی که باید به ردیف بیان
    value_vars=["NA", "EU", "JP", "Other"],
    var_name="Region",
    value_name="Sales"
)
print(vg2)
