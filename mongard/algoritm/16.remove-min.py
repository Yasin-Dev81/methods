"""
- remove-min
    * یک لیست از اعداد را گرفته و کوچکترین عضو را حذف میکند

"""


def remove_min(stack):
    if len(stack)==0:
        return stack

    min = stack[0]
    for i in stack:
        if i<min:
            min = i

    stack.remove(min)
    return stack

print(remove_min([4, 5, 6, -1, 8, 9, -3, 5]))
