"""
- اگه بخوایم بجای یوزر پسورد از ایمیل پسورد برای لاگین استفاده کنیم
- اول میره با یوزرنیم تست میکنه اگه نشد با کاستومی که ساختیم تست میکنه
- یعنی اول با یوزرنیم تلاش میکنه بعد با ایمیل

"""

# 1
# create "./accounts/authenticate.py" and write bellow code
from django.contrib.auth import get_user_model

class EmailBackend:
    def authenticate(self, request, email=None, password=None):
        try:
            user = get_user_model().objects.get(email=email)
            if user.check_password(password):
                return user
            return None
        except get_user_model().DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None

# 2
# open "./config/settings.py" and write bellow
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authenticate.EmailBackend', # <--------------
]
