"""
- چارت دایره‌ای

"""

from matplotlib import pyplot as plt
import numpy as np


Depts = ["CDGS", "IT", "Payroll", "R&D", "Sales & Marketing"]
# برای اینکه خط برگرده سرجای اولش داده‌ی اول رو آخر هم اضافه میکنیم
rp = [30, 15, 25, 10, 20] + [30]
ra = [32, 20, 23, 11, 14] + [32]

fig = plt.figure(figsize=(6, 10))
# تنظیم تایپ پروجکشن برای نوع دایره‌ای چارت
ax = fig.add_subplot(projection="polar")

# ساخت لیبل‌ها و خطوط شعاع
lines, labels = ax.set_thetagrids(range(0, 360, int(360/len(Depts))), labels=Depts)

# مشخص کردن زاویه‌های دیتا (رادیان)
theta = np.linspace(0, 2*np.pi, len(rp))
# rp
ax.plot(theta, rp, label="Plan")
ax.fill(theta, rp, color="b", alpha=0.1)
# ra
ax.plot(theta, ra, label="xx")
ax.fill(theta, ra, color="r", alpha=0.1)


plt.show()
