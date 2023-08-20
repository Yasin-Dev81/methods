"""exception handling"""

from msilib.schema import Error


SyntaxError # ارور نماد ------------> a = 2 3, b = sfsd'
NameError # وجود نداشتن نام ------------> a = 2 + c
IndexError # وجود نداششتن اندیس مورد نظر
ValueError # مقدار مورد نظر در لیست وجود ندارد
KeyError # کلید دیکشنری مورد نظر وجود ندارد
ZeroDivisionError # ارور تقسیم بر صفر ----------------> a = 5/0
ModuleNotFoundError # ماژول یا پکیج مورد نظر وجود ندارد

try :
    print ("sdk")
except :
    print ("error!")

try :
    print (sdfd)
except NameError :
    print ("NameError!")
except ValueError :
    print ("ValueError!")

def calc_income(income) :
    assert 10<=income , "income should not be a nagetive number !"
    print (income)

try :
    calc_income(2)
except AssertionError as e :
    print ("error in calc_income(2) :", e)
except NameError as e :
    print ("error in calc_income(2) :", e)
except Exception as e :
    print ("some other error :", e)
else : # همانند الس فور -----> اگر اروری نداشته باشد اجرا میشود
    print ("calc_income is ok:)")
finally : # در نهایت هرچه شد اجرا می شود
    print ("calc_income finished:)")

x = False
if x :
    pass
else :
    raise Exception("error!")
