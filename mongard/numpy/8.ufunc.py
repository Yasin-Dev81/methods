"""
https://numpy.org/doc/stable/reference/ufuncs.html

- vectorization
    - اجرای کد توسط c

- ufunc
    - run func with C lang

- Methods
    - 5 تان
    - رفتار یوفانکشن‌ها رو عوض میکنن
    - reduce
        - در امتداد یک محور، ابعاد آرایه را یک بار کاهش می دهد.
    - accumulate
        - جمع آوری نتیجه اعمال عملگر برای همه عناصر.
    - reduceat
        - کاهش را با برش های مشخص روی یک محور انجام می دهد.
    - outer
        - ...
    - at
        - عملیات بدون بافر را در عملوند 'a' برای عناصر مشخص شده توسط 'شاخص ها' انجام می دهد.

"""
import numpy as np

a = np.arange(10000)
print("sum of a:", np.sum(a))


b = np.array([1, 6, 4])
c = np.array([7, 6, 2])

## available-ufuncs
# https://numpy.org/doc/stable/reference/ufuncs.html#available-ufuncs
"+"
x = b + c # nobe
y = np.add(b, c) # legendery
"-"
np.subtract(b, c)

# Methods

# جمع ایتم‌های داخل یک آرایه با متود
sum_a = np.add.reduce(b)
print("sum of a:", sum_a)

# جمع تجمعی
t = np.add.accumulate(b)
print("tajamoii:", t)

# جمع هر ایتم اولی در همه آیتم‌های دومی
tt = np.add.outer(b, c)
print("outer:", tt)
