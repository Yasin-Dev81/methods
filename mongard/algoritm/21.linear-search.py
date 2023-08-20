"""
- linear-search (sequential search)
    * هر عنصر را با مقداری که ما به دنبال آن هستیم مقایسه می کند. اگر هر دو مطابقت داشته باشند، عنصر پیدا می شود و الگوریتم موقعیت ایندکس کلید را برمی گرداند.
    *
"""

def linear_search(array, element):
    for i in range(len(array)):
        if array[i]==element:
            return i
    return -1

print(linear_search([3, 6, 1, 7, 5], 7))
