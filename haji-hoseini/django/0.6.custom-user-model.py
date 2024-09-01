# custom user model
# اول هر پروژه هنگام ساخت دیتابیس انجام میدهیم
# عوض کردن user model 
# شخصی سازی دیتابیس پیش ساخته یوزر های جنگو

# 0
"""python manage.py startapp accounts"""

# 1
# add ((accounts)) in ((setting))

# 2
# باز کردن فایل زیر
"""./accounts/models.py"""

# 3
# ساخت کلاس با استایل زیر برای دیتابیس
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    # هرچی که میخواهیم در کنار یوزر و پسورد ذخیره کنیم
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return "%s with %s year old" % (self.username, self.age)

    def get_absolute_url(self):# بعد از اضافه شدن به دیتابیس به لینک قید شده ریدایرکت میشود
        return reverse('[url-name]', args=[self.id, ])



# 4
# ارجاع دادن به تنظیمات جنگو
# .\config\settings.py 
AUTH_USER_MODEL = 'accounts.CustomUser'

# 5
# create forms
# باز کردن فایل زیر
"""./accounts/forms.py"""

# 6
# نوشتن کد زیر
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('age', )
        # or: fields = ('username', 'email', 'age', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = UserChangeForm.Meta.fields + ('age', )
        # or: fields = ('username', 'email', 'age', )


# 7
# add to admin
# باز کردن فایل زیر
"""./accounts/admin.py"""

# 8
# نوشتن کد زیر
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'age']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )


# 9
# ساخت مایگریت
"""python manage.py makemigrations accounts"""


# 10
# مایگریت کردن
"""python manage.py migrate"""

# 11
# ساخت سوپر یوزر
"""python manage.py createsuperuser"""


# 12
# create signup in accounts view
# and create 'registration\signup.html' & 'registration\login.html' file
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration\signup.html'
    success_url = reverse_lazy('login')

# 13
# add to accounts url
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup_url')
]

