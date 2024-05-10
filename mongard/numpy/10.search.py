"""
- sorting, searching, counting


"""
import numpy as np


surnames = ("hety", "mety", "hety")
first_names = ("hety", "mety", "mety")

x = np.array([3, 2, 1, 4, 5, 7])

a = np.array([
    [1, 4, 2],
    [3, 1, 5]
])

# سورت در آرایه جدید
np.sort(a, axis=0) # sort in column
# سورت در همان آرایه
a.sort()

# سورت براساس کلیدهای ورودی
b = np.lexsort((first_names, surnames))
print(b) # returned index

# ایندکس‌های آرایه مرتب شده
c = np.argsort(x)
print(c)

# در کدام ایندکس ایتم را وارد کنیم تا ترتیب به هم نخورد
ss = np.sort(x)
print(np.searchsorted(ss, 6)) # returned index

# ایندکس ماکسیمم
print(np.argmax(x))
print(np.argmax(a, axis=0))

# ایندکس مینیمم
print(np.argmin(x))

# گرفتن آیتم با شرط
print(np.extract(np.mod(x, 3) == 0, x))

# ایندکس اونایی که صفر نیستن
print(np.nonzero(x))
# almose use for True/False
# ایندکس‌های آیتم‌هایی که بزرگتر از 3 هستن
print(np.nonzero(x>3))
# تعداد ایتم‌هایی که بزرگتر از 3 هستن
print(np.count_nonzero(x>3))
