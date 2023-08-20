# فراموشی رمز عبور
# ex templates in "11.templates" file

# 1
# open "./config/setting.py" and write bellow code
# Email Config
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 2
# ساخت فایل های زیر
"""./templates/registration/password_reset_form.html"""
"""./templates/registration/password_reset_done.html"""
"""./templates/registration/password_reset_confirm.html"""
"""./templates/registration/password_reset_complete.html"""

# 3
# نوشتن کد مورد نیاز تمپلیت
# ex: 11.password_change_done.html
# ex: 11.password_reset_form.html
# ex: 11.password_reset_done.html
# ex: 11.password_reset_confirm.html
# ex: 11.password_reset_complete.html

# 4
# تغییر متن ایمیل ارسالی
# ساخت فایل های زیر
"""./templates/registration/password_reset_email.html"""

# 5
# نوشتن کد مورد نیاز تمپلیت
# ex: 11.password_reset_email.html
