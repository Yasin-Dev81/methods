"""
- نمودارهای میله‌ای

"""
from matplotlib import pyplot as plt
import numpy as np


years = list(range(2010, 2020))
salaries = list(range(100, 600, 50))
price = list(range(1000, 1400, 40))


## میله‌ها روی هم
plt.bar(years, price, width=0.3)
# mix
# plt.plot(years, salaries, color="y")
plt.bar(years, salaries)

# نامگذاری محور‌ها
# plt.xticks(years, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
plt.show()

## میله‌ها کنار هم

# ساختن عدد به اندازه‌ی محور x
x = np.arange(len(years))
# تعیین پهنا
width = 0.3

plt.bar(x, price, width=width)
plt.bar(x-width, salaries, width=width)
# خوشگلتر
# plt.bar(x+width/2, price, width=width)
# plt.bar(x-width/2, salaries, width=width)

plt.show()


# میله‌ای افقی
plt.barh(years, salaries)
plt.show()
