"""
- pie chart

"""

from matplotlib import pyplot as plt


# لازم نیست مجموعشون 100 بشه
market_share = [43, 32, 21, 19]
companies = ["apple", "samsung", "sony", "other"]

plt.pie(
    market_share,
    labels=companies,
    # جدا کردن قسمتی از باقی نمودار
    explode=[0, 0.1, 0, 0],
    colors=["b", "k", "y", "g"],
    # شعاع دایره
    radius=1.5,
    # نمایش درصد
    autopct="%1.2f%%",
    # فاصله لیبل از چارت
    labeldistance=1.5,
    # زاویه‌ای که نمودار شروع به کشیدنش کنه
    startangle=90,
    counterclock=False # موافق عقربه‌های ساعت
)
plt.show()
