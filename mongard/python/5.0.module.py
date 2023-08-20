"""
- ماژول‌های پایتون
    * فایل‌های پایتونی هستن که در کدمون میخوایم ازشون استفاده کنیم

main folder
|
-- a.py
|
-- folder1
    |
    -- b.py
    |
    -- c.py

- b.py:
    * import c
    * from c import ...
    * import a
    * from a import ...
- a.py:
    * import folder1.b
    * from folder1.b import ...
    * import folder1.c 
    * from folder1.c import ...


- دسترسی به ماژول‌ها از دایرکتوری دیگر
    * اضافه کردن مسیر‌ها
        ~ 000x
    * اضافه کردن ماژول به مسیر پایتون
"""
# 000x
import sys
sys.path.append('...path...')

