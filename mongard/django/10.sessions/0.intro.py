"""
- sessions (cookie)
    * اطلاعاتی هستن که میخواهیم داخل مرورگر کاربر ذخیره کنیم تا براساس اون کاربر رو بشناسیم
    * چه زمانی سشن‌ها ذخیره میشه؟
        ~ زمانی که در یکی از متغیرها تغییری ایجاد کنیم
        ~ for dict:
            \ request.session['foo'] = {}
            \ request.session['foo']['bar'] = 'baz'
            \ request.session.modified = True

- انواع سشن
    * database-backed sessions
        ~ دیتا رو تو دیتابیس اصلی ذخیره میکنه و هشش رو تو مرورگر کاربر
    * cached sessions
        ~ دیتا رو تو سیستم کش مث ردیس ذخیره میکنه و هشش رو تو مرورگر کاربر
        ~ بهترین سرعت
    * file-based sessions
        ~ دیتا رو تو یه فایل ذخیره میکنه و هشش رو تو مرورگر کاربر
    * cookie-based sessions
        ~ دیتا رو تو مرورگر کاربر هش میکنه

"""
