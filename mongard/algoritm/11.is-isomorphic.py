"""
- is isomorphic
    * دو استرینگ را گرفته و مشخص میکند که آیا این دو رشته با یکدیگر متقارن هستند یا نه
    * اگه تکرار داشتیم باید همون تطابق قبلی ادامه پیدا کند

"""


def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    dict = {}
    set_values = set()
    for i in range(len(s)):
        if s[i] not in dict:
            if s[i] in set_values:
                return False

            dict[s[i]] = t[i]
            set_values.add(t[i])

        elif dict[s[i]] != t[i]:
            return False

    return True

print(is_isomorphic('foo', 'baa'))
