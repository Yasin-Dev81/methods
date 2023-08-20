"""
- search insert
    * این الگوریتم یک لیست و عدد را گرفته و در صورت وجود عدد در لیست مکان آن را مشخص میکند اما اگر عدد در لیست وجود نداشته باشد، مشخص میکند که اگر قرار بود عدد وجود داشته باشد در کجا قرار میگرفت.

"""

def search_insert(array, val):
    low = 0
    high = len(array) - 1
    mid = high // 2

    while low<=high:
        if val>array[mid]:
            mid += 1
            low = mid
        else:
            mid -= 1
            high = mid
    return low

print(search_insert([1, 2, 3, 5], 4))
