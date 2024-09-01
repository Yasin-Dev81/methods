"""
- روش شی‌گرا
The explicit API

- هر فیجر شامل چند اکسیس هست
- figure = axis1 + axis2 + axis3 + ...
- هر اکسیس یه نمودار میتونه باشه.

"""
from matplotlib import pyplot as plt
import numpy as np


data = np.arange(0, 100, 30)


## method 1
fig = plt.figure(
    facecolor="b",
    # تنظیم سایز فیجر (اینچ)
    figsize=(8, 8)
)
fig.suptitle("haji")

# ساخت اکسیس
# تعداد ردیف، تعداد ستون, ایندکس این اکسیس
ax1 = fig.add_subplot(2, 2, 1, facecolor="y", title="sin")
ax1.plot(data, np.sin(data))


ax2 = fig.add_subplot(2, 2, 2, facecolor="r", title="cos")
ax2.plot(data, np.cos(data))


ax3 = fig.add_subplot(2, 2, 3, facecolor="r", title="tg")
ax3.plot(data, np.tan(data))


# تنظیم فاصله‌ها
fig.subplots_adjust(
    # فاصله بین ستون‌ها
    wspace=1,
    # فاصله بین ردیف‌ها
    hspace=1,
)

plt.show()


## method 2
fig, ax = plt.subplots()
ax.plot(data, np.sin(data))
