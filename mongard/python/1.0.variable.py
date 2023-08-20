
# ساخت متغیر
n = 30
a = "salam"
b = True
c = False

# حذف متغیر
del n


"""
- قوانین نام گذاری:
    * نام متغیر باید با حروف انگلیسی یا ـ شروع بشه
    * نام متغیر فقط شامل حروف الفبا و عدد و ـ باشه
    * نام متغیر به حروف بزرگ و کوچیک حساسه
    * کلمات کلیدی رزرو شده در پایتون نمیتونن به عنوان متغیر انتخاب بشن
    * نام متغیر نمیتونه دارای فاصله باشه

- روش‌های نام گذاری:
    * Camel Case > numberOfCollege
    * Pascal Case > NumberOfCollege
        + کلاس‌ها
    * Snake Case > number_of_college
        + توابع
        + نام متغیر‌ها

- راهنمای سبک برای کد پایتون : PEP8

"""

# هویت متغیر‌ها
id_of_a = id(a)
print(id_of_a)

# متغیر ثابت
HOST = "google.com"

"""
- تایپ‌های متغیرها:
    * int
    * float
    * str
    * bool
"""

# بک‌اسلش باعث بی معنی شدن کارکتر بعدی میشه
# \n : newline(enter)
x = 'you can\'t read next line \\n:) \n:))'
print(x)
