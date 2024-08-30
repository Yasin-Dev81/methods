"""
- نمایش جدول
توی این مثال با چارت میکسش میکنیم

"""
from matplotlib import pyplot as plt
import numpy as np


rows = ["2011", "2012", "2013", "2014", "2015"]
columns = ["7Ah", "35Ah", "40Ah", "135Ah", "150Ah"]
data = [
    [75, 144, 114, 102, 108],
    [90, 126, 102, 84, 126],
    [96, 114, 75, 105, 135],
    [105, 90, 150, 90, 75],
    [90, 75, 135, 75, 90],
]


# انتخاب پلت رنگی
colors = plt.cm.summer(
    # ساخت عدد به تعداد نیاز
    np.linspace(0, 0.5, len(rows))
)


# ساخت لوکیشن میله‌های چارت
index = np.arange(len(columns)) + 0.3

# استارت چارت از چه عرضی باشه
# میخواهیم تجمعی پیش بریم پس هر دفعه به این اعداد قبلی رو اضافه میکنیم
y_offset = np.zeros(len(columns))


fig, ax = plt.subplots()

cell_text = []

# آجر میچینیم میریم بالا
for row in range(len(data)):
    plot = ax.bar(index, data[row], 0.5, bottom=y_offset, color=colors[row])
    y_offset += data[row]
    cell_text.append(["%1.1f"%x for x in y_offset])

    # نوشتن عدد هر آجر
    i = 0
    for rect in plot:
        ax.text(rect.get_x() + rect.get_width()/2, y_offset[i], "%1.1f" % int(y_offset[i]), ha="center", va="bottom")
        i += 1



# ساختن تیبل
the_table = ax.table(
    cellText=cell_text,
    rowLabels=rows,
    colLabels=columns,
    rowColours=colors,
    # colColours=colors,
    loc="bottom",
    cellLoc="center"
)

# حذف لیبل‌های x
plt.xticks([])

# کامپکت کردن چارت برای اینکه تو سایز مشخص شده جا بشه
plt.tight_layout()

plt.show()
