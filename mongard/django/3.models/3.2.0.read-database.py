"""
- طریقه خوندن یه مادل
    * با کوعری
    * with QuerySet
        ~ تنبل هستن
        ~ یعنی تا زمانی که واقعا بهش نیاز نداشته باشیم جنگو اجراش نمیکنه
    * ModelName.objects.[defs()]

- defs() :
    * all()
        ~ همه اطلاعات
    * filter(...)
        ~ اطلاعات فیلتر شده
    * first()
        ~ اولین دیتا
    * order_by('...')
        ~ مرتب کردن براساس فیلدهای داده شده
    * order_by('?')
        ~ رندمیک کردن ترتیب دیتا
    
    

- حالاتی که جنگو کوعری رو اجرا میکنه
    * iteration: حلقه
    * slicing
    * Pickling/Caching
    * repr()
    * len()
    * list()
    * bool()        

"""

# تو کد زیر جنگو فقط یه بار به دیتابیس وصل شده تا بهینه تر باشه
q = 'ModelName'.objects.fiter('...')
q = q.filter('...')
print(q)

