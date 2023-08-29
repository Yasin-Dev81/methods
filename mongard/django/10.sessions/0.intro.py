"""
- sessions (cookie)
    * اطلاعاتی هستن که میخواهیم داخل مرورگر کاربر ذخیره کنیم تا براساس اون کاربر رو بشناسیم
    * چه زمانی سشن‌ها ذخیره میشه؟
        ~ زمانی که در یکی از متغیرها تغییری ایجاد کنیم
        ~ for dict:
            \ request.session['foo'] = {}
            \ request.session['foo']['bar'] = 'baz'
            \ request.session.modified = True

"""
