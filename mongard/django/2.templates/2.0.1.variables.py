"""
- نمایش متغیرها:
    * با قرار دادن متغیر در {{...}} میشه نمایششون داد

- ارسال متغیرها از ویو:
    * with context in render()

def ... (request, ...):
    ...
    return render(
        request,
        context={
            '...': '...'
        }
    )


"""