"""
- برای اکسل این دو پکیج لازمه نصب بشه
pip install xlrd openpyxl

"""
import pandas as pd


nobel = pd.read_json("./files/prize.json")

# add laureates to alls
# اگه لوریتیتز تو هر ردیف نبود بهش اضافه کنه
nobel["prizes"].apply(lambda i: i.setdefault("laureates", []))

winners = pd.json_normalize(
    # ستونی که توش جیسونه
    nobel["prizes"],
    # کلیدی که توش باز یه جیسون دیگه‌س
    record_path="laureates",
    # ستون‌هایی که حتما بسازه
    meta=["year", "category"]
)

print(winners)


# convert to json
# بصورت ستونی
winners.to_json()

# بصورت ردیفی
winners.to_json("./files/news.json", orient="records")

# save csv
# ذخیره بدون ایندکس‌ها
winners.to_csv("./files/winners.csv", index=False, columns=["year", "category"])


## Excel
# پکیج‌های بالا رو بنصب
# like read_csv

pd.read_excel(
    "./files/Multiple Worksheets.xlsx",
    # شماره ایندکس یا نام شیت موردنظر
    # if sheet_name=None: returned all sheets as dict
    sheet_name=[1]
)

# دخیره کردن در اکسل
# تک شیت‌ها
winners.to_excel()

# چند شیتی
with pd.ExcelWriter("./files/winners.xlsx") as writer:
    winners.head().to_excel(excel_writer=writer, sheet_name="head", index=False)
    winners.tail().to_excel(excel_writer=writer, sheet_name="tail", index=False)
