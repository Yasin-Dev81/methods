"""
- seaborn
    - برای نمایش داده‌های آماری
    - برای حجم اطلاعات زیاد استفاده میشه

- datasets in seaborn
    - استفاده از دیتاست‌های خود سیبورن
    - لود با پانداز

"""
import seaborn as sns
import matplotlib.pyplot as plt

# تنظیم تم
sns.set_theme(context="paper", style="dark", palette="colorblind")

# لود کردن از دیتاست‌های خود سیبورن
tips = sns.load_dataset("tips")

sns.relplot(
    data=tips,
    x="total_bill",
    y="tip",
    # جدا کردن چارت‌ها
    col="time",
    # کلاس بندی (با رنگ و استایل)
    hue="smoker",
    style="smoker",
    # تنظیم سایز
    size="size"
)

plt.show()
