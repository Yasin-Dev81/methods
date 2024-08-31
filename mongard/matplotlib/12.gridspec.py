"""
- gridspec
    - برای چسبوندن چندتا چارت به هم
    - تبدیل چند چارت به یک چارت
    - تنظیم سایز سابپلات

"""
from matplotlib import pyplot as plt
from matplotlib import gridspec
import numpy as np


# constrained_layout: برای فاصله بین چارت‌ها
fig = plt.figure(constrained_layout=True)
# یه فضای 3*3 میسازیم
gs = fig.add_gridspec(3, 3)


# ردیف اول و کل ستون‌هاش
ax_1 = fig.add_subplot(gs[0, :])
ax_2 = fig.add_subplot(gs[1, :2])
ax_3 = fig.add_subplot(gs[1:, -1])
ax_4 = fig.add_subplot(gs[-1, 0])


plt.show()
