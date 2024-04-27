"""
"""
import numpy as np

# ساخت رندم ایتم
a = np.empty((3, 4), dtype=np.int8)
print(a)

p = ([1, 2, 3], [4, 5, 6])
a1 = np.empty_like(p, shape=(3, 2))
print(a1)

# ساخت ارایه همانی
b = np.eye(4, 5, -1)
print(b)

# eye_like هم داره

# ساخت ارایه همانی با عرض و طول مساوی
c = np.identity(4)
print(c)

# ارایه با ایتم‌های مساوی یک
d = np.ones((2, 3, 4))
# ارایه با ایتم‌های مساوی صفر
e = np.zeros((2, 3, 4))

# ارایه با ایتم‌هایی که مشخص کردیم
f = np.full((3, 3), 8)
print(f)

# تو یه رنج ارایه ایجاد میکنه
g = np.arange(90)
g1 = np.arange(1, 10)
print("reshaped of arange 1-10", g1.reshape((3, 3)))
print(g)
