"""
- مراحل داخل بروکر
    * درخواست وارد میشود
    * --> exchange
    * تصمیم گرفته میشود که داخل کدام صف قرار بگیرد
    * Binding --> queue
    * اجرا به ترتیب صف‌ها

- انواع exchange
    * Direct Exchenge
        ~ با درخواست اسم صف هم ارسال میشه و براساس اون وارد صف موردنظر میشه
    * Fanout Exchenge
        ~ درخواست رو به تمام صف‌ها ارسال میکنه
    * Topic Exchenge
        ~ براساس الگویی که ما تعیین میکنیم ارسال میشه
    * Headers Exchenge
        ~ به صورت دیکشنری الگو رو تعیین میکنیم

- channel
    * برای اتصال‌های بهینه‌تر بخش‌ها به چنل‌ها وصل میشن تا تعداد کمتری کانکشن با سرور برقرار بشه
"""