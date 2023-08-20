"""
- rotate
    * به تعداد مشخص از کارکترهای اول استرینگ را برداشته و به آخر استرینگ میبرد

"""

def rotate(s, k):
    k = k%len(s)
    double_s = s+s
    return double_s[k:k+len(s)]

print(rotate('amir', 7))
