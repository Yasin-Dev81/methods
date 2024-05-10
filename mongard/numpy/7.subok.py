"""
- subok
    - از کلاس قبلی استفاده بشه یا نشه
مثلا اگه یه
masked array
داخل یه آرایه بذاریم کلاسش عوض بشه یا همون قبلی بمونه
# ex 2

- order types
    - K
        - auto
    - A
        - auto
    - C
        - C lang
        - دخیره ردیفی
    - F
        - Fortran lang
        - ذخیره ستونی

"""
import numpy as np
import numpy.ma as ma


x = np.array(
    [],
    # اگه از این آرایه جایی استفاده شده، اون جدیده کپی باشه
    # روی ارایه اول تغییری ایجاد نشه
    # ex 1
    copy=True,
    # از کلاس قبلی استفاده بشه یا نشه
    subok=True,
    #
    order="k"
)

# ex 1
a = np.array([1, 2, 3])
b = np.array(a, copy=False) # همون قبلی میشه (کپی نیست)

# ex 2
c = ma.masked_array([1, 2, 3]) # MaskedArray
d = np.array(c) # ndarray
e = np.array(c, subok=True) # MaskedArray
print("type of c, d, e:", type(c), type(d), type(e))
