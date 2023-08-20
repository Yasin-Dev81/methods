"""
- Polynomial Time
    * O(n**x)
    * O(n**3)

"""
# ex:
nums = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(collection):
    length = len(collection)
    for i in range(length-1):
        swapped = False
        for j in range(length-1-i):
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
        if not swapped:
            break
        return collection

print(bubble_sort(nums))
