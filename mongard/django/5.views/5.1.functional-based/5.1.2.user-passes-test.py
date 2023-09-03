"""
- متدهایی که لازم است به‌غیر از لاگین چیز دیگه‌ای هم انجام بدن
- بیشتر برای دسترسی کاربره

"""
# ex:
from django.contrib.auth.decorators import user_passes_test


def email_check(user):
    return user.email.endwith('@gmail.com')

@user_passes_test(email_check)
def my_view(request):
    pass
