"""
- first-occurrence
    * اولین ایندکس المان موردنظر در آرایه را برمیگرداند
"""

def binary_search(array, element):
    low, high = 0, len(array)-1

    while low<=high:
        mid = (high+low)//2
        val = array[mid]
        if val==element:
            return mid
        elif val<element:
            low = mid
        else:
            high = mid
    return -1

print(binary_search([2, 3, 4, 6, 12, 16, 18, 19], 12))
