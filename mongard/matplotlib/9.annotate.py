"""
- ساخت فلش برای اشاره به قسمت از چارت

"""

from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 20, 1000)


fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

ax1.plot(x, np.cos(x))
ax2.plot(x, np.cos(x))

# مساوی کردن محور y
ax1.axis("equal")
ax2.axis("equal")


# مدل معمولی
ax1.annotate(
    "max",
    # لوکیشن
    xy=(6.28, 1),
    # لوکیشن متن
    xytext=(10, 4),
    # ساخت فلش
    arrowprops={
        "facecolor": "y",
        # فاصله دادن از دوطرف
        "shrink": 0.05,
    },
)
# مدل استایل دار
ax2.annotate(
    "min",
    xy=(5*np.pi, -1),
    xytext=(2, -6),
    arrowprops={
        # استایل
        "arrowstyle": "->",
        # نوع خط
        # استایل, میزان انحنا, زاویه شروع, زاویه اتمام
        "connectionstyle": "angle, rad=90, angleA=5, angleB=45"
    },
)


plt.show()
