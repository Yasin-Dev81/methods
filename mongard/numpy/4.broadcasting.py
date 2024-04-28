"""
- عملیات‌های ریاضی

- broadcasting
    - ارایه‌ای که کوچکتر هست رو پخش میکنه تو آرایه بزرگتر
    - a + 1

"""
import numpy as np

a = np.array(
    [
        [1, 2, 3],
        [9, 5, 11]
    ]
)
b = np.array([[6, 8, 5]])
c = np.array([[8, 16, 7]])

# جمع متناضر آیتم‌ها
print("a+b", a+b)
print(a+1)

# مقایسه متناضر ایتم‌ها
print("a == b", a == b)

# مقایسه ارایه‌ها
print("a eaual b:", np.array_equal(a, b))

# جمع آیتم‌ها
print("sum of a", np.sum(a), a.sum())
# sum with axis
print("sum of a (axis=0)", a.sum(axis=0))

# min and mux
print("min and mux", a.min(), a.max())
