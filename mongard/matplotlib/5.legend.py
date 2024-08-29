"""
- locations
    - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend

"""
from matplotlib import pyplot as plt
import numpy as np


x = np.arange(0, 100, step=30)

plt.plot(x, np.sin(x), label="sin")
plt.plot(x, np.cos(x), label="cos")
plt.plot(x, np.tan(x), label="tg")

plt.legend(
    # لوکیشن معمول
    # loc="center",
    # لوکیشن مختصاتی
    loc=(0, 0),
    # تعداد ستون‌ها
    ncol=2,
    # مشخص کردن فونت، سایز و ..
    prop={
        "family": "serif",
        "size": 14,
        "style": "italic"
    },
    edgecolor="b",
    # تیز کردن باکس لجند
    fancybox=False,
    # رنگ بکگراند
    facecolor="y",
    # تایتل لجند
    title="لجند باشه",
    # فاصله از خطوط باکس (میاد وسط‌تر)
    borderpad=2,
    # فاصله ردیف‌ها
    labelspacing=2,
    # فاصله ستون‌ها
    columnspacing=2,
)

plt.show()
