"""

"""
import numpy as np
from math import pi

# ساخت اعدادی که فاصله یکسانی از همدیگه دارن
# retstep: نشان دادن فاصله اعداد
a = np.linspace(1, 99, num=5, retstep=True)
print(a)

# با ابجکت‌های ایتریبل آرایه میسازه
l = [i*i for i in range(1, 11)]
b = np.fromiter(l, dtype=np.int8)
print(b)

# با استرینگش هم هست
c = np.fromstring("1,2,3,4", dtype=np.int8, sep=",")
print(c)

# تبدیل درجه به رادیان
d = np.radians(180)
print(d)

# تبدیل رادیان به درجه
e = np.degrees(2*pi)
print(e)
