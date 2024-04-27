"""

- ساختار داده در نامپای
    - آرایه

- array
    - یه کانتینر هستش که چندتا آیتم رو داخل خودش نگه میداره
    - میتونه چند بعدی باشه
    - همه آیتم‌ها یه نوع‌اند
        - مثلا همه int
        - اگه فرق کنن تا جایی که بتونه یکیشون میکنه

- ابعاد
    - 0D
        - Non axis
    - 1D
        - (0, ) axis
    - 2D
        - (0, 1, ) axis
    - 3D
        - (0, 1, 2, ) axis


- unsignedinteger (uint)
    - نا منفی

"""
import numpy as np

# ساخت آرایه
a = np.array([2, 8, 5])
print(a, type(a))

b = np.array(
    [
        [2, 5],
        [6, 8]
    ]
)

c = np.array(2)

# ابعاد آرایه
# عمق
print("ndom of a", a.ndim)
print("ndim of b", b.ndim)
print("ndim of c", c.ndim)

# تعداد ردیف و ستون
print("shape of b", b.shape)

# دیدن تایپ ایتم‌ها
print("dtype of a", a.dtype)


# ساخت ارایه با مشخص کردن تایپ
y = np.array([2, 5], dtype=np.uint8)
x = np.uint8([2, 5])

print(x, y)
