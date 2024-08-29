from matplotlib import pyplot as plt
import numpy as np


## stackplot
# طرح پشته ای
year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
population_by_continent = {
    "africa": [228, 230, 220, 225, 240, 300, 310, 280],
    "americas": [300, 330, 120, 335, 350, 400, 410, 250],
    "asia": [154, 280, 230, 251, 310, 340, 370, 380],
    "europe": [164, 330, 210, 125, 340, 320, 370, 380],
}

plt.stackplot(
    year,
    population_by_continent.values(),
    labels=population_by_continent.keys()
)
plt.legend()
plt.show()


## histogram
x = np.random.randint(140, 200, 500)
y = np.random.randint(140, 200, 300)

plt.hist(
    x,
    # تعداد ستون
    bins=8,
    # بصورت رنج هم میتونیم ارسال کنیم
    # bins=(140, 150, 160, 170, 180, 190, 200),
    # رنگ دور نمودار
    edgecolor="k",
    # افقی کردن نمودار
    # orientation="horizontal",
    # تایپ هیستوگرام
    # histtype="stepfilled"
)
plt.show()

# نمایش چند هیستوگرام باهم
plt.hist(
    [x, y],
    # روی هم
    histtype="barstacked",
    # کنار هم
    # histtype="bar",

)
plt.show()


## scatter
countries = ["Germany", "Turkey", "Vietnam", "Egypt", "Pilippines", "Japan", "Mexico", "Russia"]
population = np.random.randint(10_000_000, 50_000_000, len(countries))
size = population/10**5

plt.scatter(
    population,
    countries,
    # اندازه‌ی هر دایره
    s=size,
    # رنگ چارت
    # رنگ کل ثابت
    # c="r",
    # رنگ متغیر
    c=size,
    # تنظیم طیف رنگی
    cmap="summer",
    # میزان شفافیت دایره‌ها
    alpha=0.5,
    edgecolors="y",
    # عوض کردن مارکر (دایره، مربع و ...)
    marker="s"
)
# نمایش طیف رنگی در کنار چارت
plt.colorbar()
plt.show()
