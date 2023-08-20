"""
- raise
    * وقتی میخوایم خودمون یه استثنا نمایش بدیم

"""

class CustomErrorName(Exception):
    pass

if True:
    raise CustomErrorName('for test')