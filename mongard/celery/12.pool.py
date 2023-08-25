"""
- انواع تسک‌ها
    * CPU bound
        ~ تسک مبتنی بر محاسبات سی‌پی‌یو است
    * I/O bound
        ~ وقتی تسک مبتنی بر ارسال درخواست به دیگر میکروسرویس‌هاست
        ~ بیشترین اتلاف وقت آن مربوط به دریافت پاسخ است و سی‌پی‌یو در آن بیکار است

- concurrency
    * تعداد تسک‌هایی که ورکر همزمان انجام می‌دهد

- execution pool
    * استخریست که پراسس‌های سلری در آن اجرا میشوند
    * انواع آن
        ~ prefork
            \ for [CPU bound]
            \ چندتا چندتا تسک‌ها رو اجرا میکنه
            \ with multiprocessing
        ~ solo
            \ for [CPU in...] (whole cpu)
            \ دونه دونه تسک‌ها رو اجرا میکنه
            \ وقتی حجم زیادی از سی‌پی‌یو رو واسه یه تسک لازم داریم
        ~ eventlet
            \ for [I/O bound]
            \ "pip instll eventlet"
            \ with threading

- عوض کردن استخر
celery -A file_name -l info --pool=solo --concurrency=1
celery -A file_name -l info --pool=eventlet

"""
