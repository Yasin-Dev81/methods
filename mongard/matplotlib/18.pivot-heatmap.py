"""
- برای ساخت هیت‌مپ اول باید پیوت آنرا ساخت

"""
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(context="paper", style="dark", palette="colorblind")


data = sns.load_dataset("flights")
pivot = data.pivot(index="year", columns="month", values="passengers")


fig, ax = plt.subplots(figsize=(9, 6))

sns.heatmap(
    data=pivot,
    ax=ax,
    # نوشتن اطلاعات در چارت
    annot=True,
    # فرمت نمایش اطلاعات
    fmt="d",
    # فاصله بین سلول‌ها
    linewidths=0.5,
)


plt.show()
