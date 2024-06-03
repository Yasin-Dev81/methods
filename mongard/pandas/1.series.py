"""
- series
    - تک بعدی هستند

- dtype by default is: auto


"""
import pandas as pd
import numpy as np


# send list
s1 = pd.Series([1, 2, 3])
print(s1) # dtype: int

# send list (boolean)
s2 = pd.Series([True, False, False])
print("s2", s2) # dtype: bool

# send list (mix)
s3 = pd.Series([2, False, 3.4, np.nan, 5.02])
print("s3", s3) # dtype: object


## تنظیم نام ایندکس‌ها
# method 1
s3.index = ["R1", "R2", "R3", "R4", "R5"]
print("s3 (with new indexes)", s3)
# method 2
s4 = pd.Series([2, 3, 1], index=["R1", "R2", "R3"])


## dtype
# method 1
s4 = pd.Series([3, 2, 1], dtype="int8")
# method 2
s5 = pd.Series([2, 3, 1], dtype=np.uint8)


# send dict
# key: index, value: data
s6 = pd.Series({"u1": "amir", "u2": "ali", "u3": "ghasem"})


## values & indexes
print("values:", s6.values)
print("indexes:", s6.index)
print("size:", s6.size)
print("shape:", s6.shape)
print("is unique", s6.is_unique)

# ایا روند داده‌ها نزولی است
print("is monotonic (s5):", s5.is_monotonic_decreasing)
# ایا روند داده‌ها صعودی است
print("is monotonic (s4):", s4.is_monotonic_increasing)


## head
s7 = pd.Series(range(1, 501, 1))
print("head 5 (s7):", s7.head(5))

## tail
print("tail 3 (s7):", s7.tail(3))


## تعداد دیتاهایی که nan نیستن
print("count of not nan (s3):", s3.count())

# sum
print("sum (s3):", s3.sum())

## ضرب تمام ایتم‌ها در همدیگر
# با نادیده گرفتن nan
print("product (s3):", s3.product())
# بدون نادیده گرفتن nan
print("product with nan (s3):", s3.product(skipna=False))

# جمع تجمعی
print("cumsum (s3):", s3.cumsum())

# درصد تغییرات هر ایندکس
print("pct_change (s4):", s4.pct_change())

# میانگین
print("mean (s3):", s3.mean())

# خلاصه‌ای از اطلاعات مفید درباره‌ی دیتا
print("describe (s3):", s3.describe())

# کشیدن دیتا بصورت رندوم از دیتای موردنظر
print("sample (s3):", s3.sample(n=2))

# +
print("s3 + 4 =", s3+4)
