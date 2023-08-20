"""
- limit
    * هدف این الگوریتم اینست که یک آرایه را محدود کند
    * شما میتوانید مقدار بیشترین و کمترین را تعیین کنید تا نتیجه براساس محدودیت‌های شما نمایش داده شود

"""
# ex:
nums = [1, 2, 3, 4, 5]

def limit(arr, min=None, max=None):
    min_check = lambda val: True if min is None else (val>=min)
    max_check = lambda val: True if max is None else (val<=max)

    return [val for val in arr if min_check(val) and max_check(val)]

print(limit(nums, 3, 3))
