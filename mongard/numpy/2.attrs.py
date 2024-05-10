"""
- متدهای کاربردی

"""
import numpy as np


a = np.array(
    [
        [1, 2, 12],
        [6, 3, 5],
        [12, 4, 9]
    ]
)
b = np.array([12, 13, 14])
c = np.array(
    [
        [4],
        [9],
        [1]
    ]
)
d = np.array(
    [
        [8, 16, 8]
    ]
)

# تعداد ایتم‌ها
print("size of a", a.size)

# ساختار آرایه
print("shape:", a.shape)

# تغییر ساختار
a2 = a.reshape(1, 9)
a3 = a.reshape(9, 1)

print("a2:", a2, "\na3:", a3)

# indexing
print(a[0][1])
print(a[0, 1])

# slicing
print(a[:2])

# چسباندن عمودی ارایه‌ها
a4 = np.vstack((a, b))
print("a4", a4)

# چسباندن افقی ارایه‌ها
a5 = np.hstack((a, c))
print("a5", a5)

# چسباندن کلی
a6 = np.concatenate((a, c), axis=1)
print("a6", a6)
a7 = np.concatenate((a, d), axis=0)
print("a7", a7)

# جدا کردن افقی
a8 = np.vsplit(a, 3)
print("a8", a8)

# جدا کردن عمودی
a9 = np.hsplit(a, 3)
print("a9", a9)

# sort
# هر آیتم رو داخل خودش سورت میکنه
a10 = np.sort(a)
print("a10 (sorted)", a10)

# کپی از آرایه
# پایه نداره
a11 = a.copy()
# نشان دادن به یه آرایه
# پایه داره
a12 = a.view()
# نشان دادن آرایه پایه (مادر)
a13 = a12.base
print(a13)
