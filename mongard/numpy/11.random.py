"""
- types
    - RandomState
        - قدیمی و منسوخ
    - BitGenerator
    - Generator

- seed
    - یه عدد میگیره و میبره تو جنریتور
    - بعد هر چندبار که ران کنیم اعداد رندوممون عوض نمیشه

"""
import numpy as np


## RandomState
# old method
x = np.random.standard_normal(10)

## BitGenerator
# new method
# ((seed is very important...))
rng = np.random.default_rng(seed=1234)


y = rng.standard_normal(10)

# رندوم بین 2 اینتجر
# endpoint: آخری هم حساب بشه
rng.integers(10, 1000, size=(2, 3), endpoint=True)

# رندوم فلوت
rng.random((2, 2))

# انتخاب از آرایه بصورت رندوم
rng.choice([1, 2, 3, 4], size=(2, 2), replace=True, p=[0.2, 0.3, 0.4, 0.1])

# بایت رندوم
rng.bytes(3)

# عوض کردن ترتیب آیتم‌ها بصورت رندوم
x = np.array([
    [2, 8, 1],
    [4, 1, 9]
])
# آرایه جدیدی نمیسازه، همون آرایه قبلی رو تغییر میده
rng.shuffle(x, axis=1)
# آرایه جدید میسازه
y = rng.permutation(x)
