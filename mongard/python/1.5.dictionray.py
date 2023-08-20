"""
- دیکشنری
    * ذخیره اطلاعات بصورت key; value

- ویژگی‌های دیکشنری:
    * تغییر پذیرن
    * پویاس
        ~ آیتم‌هاش رو میشه کم و زیاد کرد
    * مرتب شده‌س

"""

a = {
    'key1': 'value1',
    'key2': 'value2'
}

b = dict(
    [
        ('key1', 'value1'),
        ('key2', 'value2')
    ]
)

c = dict(
    key1='value1',
    key2='value2'
)

print(a['key2'], a.get('key2'))

# اضافه کردن یه دیکشنری به دیکشنری دیگه
a.update(b)
