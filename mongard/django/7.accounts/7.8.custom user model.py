"""
- ساخت مدل یوزرها و جایگزین کردن آن با مدل پیشفرض جنگو
- پیشنهاد میشه که همیشه ساخته بشه زیرا توسعه رو راحت‌تر میکنه

- برای اینکه خیلی از کد‌ها رو دوباره ننویسیم از کلاس‌های ابسترکت آماده جنگو استفاده میکنیم
- اینکار به دو روش انجام میشه
    * AbstractBaseUser
        ~ فقط امکانات بیسیک را دارد
    * AbstractUser
        ~ امکانات بیشتری دارد

- Manager
    * قطعه کدیست که به ما اجازه میده با مدل‌هامون ارتباط برقرار کنیم
    * نرمالایز کردن ایمیل
        ~ چک کردن درست بودن ایمیل
        ~ کوچک کردن حروف بزرگ

"""
# on "./accounts/models.py"
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=255, unique=True)
	phone_number = models.CharField(max_length=11, unique=True)
	full_name = models.CharField(max_length=100)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

    # اختصاص منیجر
	objects = UserManager()

    # با چه فیلدی اعتبارسنجی بشه؟
	USERNAME_FIELD = 'phone_number'
	# فیلدهای اجباری واسه ساخت سوپریوزر
	REQUIRED_FIELDS = ['email', 'full_name']

	def __str__(self):
		return self.email

    # کاربرهایی که اجازه دارن وارد ادمین پنل بشن
    # برای اینکه رفتارش مث is_active بشه از پراپرتی استفاده میکنیم
	@property
	def is_staff(self):
		return self.is_admin


# in "./accounts/managers.py"
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self, phone_number, email, full_name, password):
		if not phone_number:
			raise ValueError('user must have phone number')

		if not email:
			raise ValueError('user must have email')

		if not full_name:
			raise ValueError('user must have full name')

        # قبل از سیو باید ایمیل رو نرمالایز کنیم
		user = self.model(phone_number=phone_number, email=self.normalize_email(email), full_name=full_name)
		# هش کردن پسورد
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, phone_number, email, full_name, password):
		user = self.create_user(phone_number, email, full_name, password)
		user.is_admin = True
		user.is_superuser = True
		user.save(using=self._db)
		return user
