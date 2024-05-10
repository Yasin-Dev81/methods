"""
- input
    - گرفتن دیتا از فایل
- output
    - ذخیره دیتا در فایل

- فرمت‌ها
    - npy
        - ذخیره یه آرایه
    - npz
        - ذخیره چند آرایه
        - zip of npy
"""
import numpy as np

a = np.array(
    [
        [4, 5, 8]
    ]
)
b = np.array(
    [
        [8, 6, 12],
        [3, 1, 4]
    ]
)

## save (output)
# allow_pickle: فشرده سازی
np.save("file_of_a", a, allow_pickle=True) # npy
np.savez("files_of_5", a, b) # npz
np.savez_compressed("compressed_files_of_5", a, b) # npz with pickle

# نامگذاری ارایه‌ها
np.savez("file_of_5_1", one=a, two=b)

# ذخیره در txt
np.savetxt("txtfile_of_a", a)

## load (input)
# allow_pickle: فقط برای فایل‌هایی که اطمینان داریم سالمند استفاده کنیم
a1 = np.load("file_of_a.npy", allow_pickle=False) # npy

c = np.load("files_of_5") # npz
# گرفتن آرایه‌ها بدون نام
c["arr_0"] # a
c["arr_1"] # b

d = np.load("file_of_5_1")
# گرفتن آرایه‌ها با نام
d["one"] # a
d["two"] # b
