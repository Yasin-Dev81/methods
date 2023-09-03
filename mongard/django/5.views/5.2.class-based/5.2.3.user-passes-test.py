"""
- متدهایی که لازم است به‌غیر از لاگین چیز دیگه‌ای هم انجام بدن
- بیشتر برای دسترسی کاربره

- روش‌ها
    * @user_passes_test(...)
    * UserPassesTestMixin

"""
# ex 1:
from django.contrib.auth.decorators import user_passes_test
from django.views import generic


def email_check(user):
    return user.email.endwith('@gmail.com')

class MyClass(generic.View):
    @user_passes_test(email_check)
    def my_view(self, request):
        pass


# ex 2:
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import generic


class MyView(UserPassesTestMixin, generic.View):

    def test_func(self):
        return self.request.user.email.endwith('@gmail.com')
