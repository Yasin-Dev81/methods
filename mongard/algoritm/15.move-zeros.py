"""
- move-zeros
    * یک لیست از کاراکترهای مختلف را گرفته و در صورت وجود عدد صفر آنها را به آخر لیست منتقل میکند

"""

def move_zeros(seq):
    result = []
    zeros = 0
    for i in seq:
        if i==0 and type(i)!=bool:
            zeros += 1
        else:
            result.append(i)
    else:
        result.extend([0]*zeros)

    return result


print(move_zeros([False, 1, 0, 1, 2, "ch", 0, 1, 3, "a"]))
