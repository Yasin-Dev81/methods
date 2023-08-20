"""
- تکه تکه کردن رشته استرینگ:
    * indexing
        ~ دسترسی به یه کاراکتر
    * slicing
        ~ دسترسی به چند کاراکتر

"""

a = 'mongard'

# indexing
print(
    'indexing:',
    a[2],
    a[-1],
    a[-3]
)

# slicing
print(
    'slicing:',
    a[2:4],
    a[:4],
    a[0:4:2]
)

# چسبوندن دوتا استرینگ
print("yasin " + "khos manesh")

# docstring
x = '...'\
    '...'\
    '...'

y = (
    '...'
    '...'
    '...'
)

z = """\
...
"""
print(x, y, z)

# بی‌معنی کردن علایم داخل استرینگ
c = r"..."
