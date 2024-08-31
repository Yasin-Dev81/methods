"""
- transformations
    - برای آدرس دهی داخل نمودار استفاده میشن
- انواع آدرس دهی:
    - data
        - براساس دیتای وارد شده به چارت لوکیشن مشخص بشه
    - axes
        - from (0, 0) to (1, 1)
        - base on axes
    - figure
        - from (0, 0) to (1, 1)
        - base on figure
    - blended
        - ترکیبی پرو

"""
from matplotlib import pyplot as plt
import matplotlib.transforms as transforms
import numpy as np


d = np.arange(0, 100, 10)


fig = plt.figure(facecolor="y")
ax = fig.add_subplot()
ax.plot(d)

## data
ax.text(2, 50, "data")

## axes
ax.text(0.5, 0.5, "axes", transform=ax.transAxes)

## figure
ax.text(0.9, 0.9, "figure", transform=fig.transFigure)

## blended
# ex: ایکس تایپ اکسیس باشه، ایگرگ تایپ دیتا
trans = transforms.blended_transform_factory(ax.transAxes, ax.transData)
ax.text(0.5, 20, "blended", transform=trans)


plt.grid()
plt.show()
