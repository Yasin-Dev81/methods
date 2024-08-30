"""
- ذخیره فیجرها

"""
from matplotlib import pyplot as plt
from matplotlib.transforms import Bbox


price = list(range(1000, 1400, 40))

fig, ax = plt.subplots()
ax.plot(price)


## کامپکت کردن
# method 1
# کامپکت کردن چارت برای اینکه تو سایز مشخص شده جا بشه
# plt.tight_layout()

# قبل از شو سیو بشه
plt.savefig(
    "./image.png",
    # method 2
    bbox_inches="tight",
    # پد دادن از اطراف
    pad_inches=1,
    # کیفیت تصویر
    dpi=100,
    # حذف بکگراند
    transparent=True
)

plt.show()


## ذخیره کردن قسمتی از فیجر
fig, ax = plt.subplots()
ax.plot(price)


plt.savefig(
    "./image.jpg",
    bbox_inches=Bbox(
        [
            [0, 0],
            [6.5, 1.2]
        ]
    )
)
plt.show()
