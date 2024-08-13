"""
- match
    - ابتدای استرینگ رو میگرده
- search
    - کل استرینگ رو میگرده اولی برمیگردونه
- findall
    - از کل استرینگ، همه رو برمیگردونه
    - return list
- finditer
    - از کل استرینگ، همه رو برمیگردونه
    - return class
- split
    - براساس پترن اسپلیت میکنه
- escape
    - حروف معنی‌دار رو اسکیپ میکنه

"""
import re

text = "hello world"

# method 1
p = re.compile(r"h.llo", flags=re.I | re.M)
x = p.match(text)
print(x, x.group(), x.span())


# method 2
y = re.match(r"h.llo", text, flags=re.I | re.M)
print(y)
