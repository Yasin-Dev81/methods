"""

- Constant Time (زمان ثابت)
    * O(1)
    * وارد شدن دیتای زیاد تاثیری در سرعت‌ش ندارد

"""

# ex:
nums = [3, 4, 5, 9, 6]

def show(list):
    if list[0] % 2 == 0:
        return True
    return False

print(show(nums))
