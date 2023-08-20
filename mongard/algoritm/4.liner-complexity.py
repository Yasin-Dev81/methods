"""

- Liner Time 
    * O(n)

"""
# ex:
nums = [2, 16, 7, 9, 8, 23, 12] # unsorted list

def show(list):
    max_num = list[0]
    for i in list:
        if i > max_num:
            max_num = i
    return max_num

print(show(nums))
