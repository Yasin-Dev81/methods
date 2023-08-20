"""
- interaction
    * تکرار یه بلوک کد
        ~ loop: حلقه

- انواع حلقه
    * while
    * for

- while
while condition:
    ...
    if ...:
        break
    ...
else:
    ...

- for
for ... in ...:
    ...
    if ...:
        continue
    if ...:
        break
    ...
else:
    ...
"""

# while
while True:
    '...'
    if True:
        break
    '...'
else:
    '...'

# for
for i in range(1, 11, 3):
    '...'
    if i%2==0:
        continue
    if not i%2==0:
        break
    '...'
else:
    '...'
