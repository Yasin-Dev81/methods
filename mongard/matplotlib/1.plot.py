"""
- روشهای رسم نمودار:
    - The explicit API
    - The implicit API
    - The pylab API

- خوشگلیاش تو عکس پیوست اومده.

- format of lines: (fmt)
    - [marker][line][color]
    - ex: o--y
"""
# The implicit API
from matplotlib import pyplot as plt


years = list(range(2010, 2020))
salaries = list(range(100, 600, 50))
price = list(range(1000, 1400, 40))


# اگه یه ورودی بدیم اون رو در محور عمودی میاره
# plt.plot(price)
# plt.show()

# تنظیم استایل
plt.style.use("bmh")

# first: x, secend: y
plt.plot(years, salaries, "o--y", label="salaries")
plt.plot(years, price, label="price", color="g", linestyle="-.", marker="D")
plt.title("prices vs. salaries")
plt.xlabel("Years")
plt.ylabel("USD")
plt.legend()
plt.grid()
# plt.savefig("./imag.png")
plt.show()
