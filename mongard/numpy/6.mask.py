"""
- Mask array
    - پوشوندن داده‌های گمشده یا نامعتبر
    - تا تو محاسبات استفاده نشن

- np.nan
    - Not a number
    - باقی رو فلوت میکنه

"""
import numpy as np
import numpy.ma as ma

a = np.arange(-3, 5)
b = np.array(
    [
        [1, 2, 3],
        [4, np.nan, 6]
    ]
)
print("a", a)
print("b", b)

# mask nan in b
# ایتم‌ها را باید مشخص کنیم
# with 0-1
m = ma.masked_array(b, mask=[0, 0, 0, 0, 1, 0])
# with True-False
m = ma.masked_array(b, mask=[False, False, False, False, True, False])

print("m", m)
print("sum m", m.sum())


# auto mask
m2 = ma.masked_invalid(b)
print("m2", m2)

# with if
m3 = ma.masked_where(a <= 0, a)
print("m3", m3)

# masked values
m4 = ma.masked_values(a, value=3)
print("m4", m4)
