"""
- تغییر فرم‌ها در پنل ادمین
    * باید حتما قبل آن فرمی در فایل فرم‌ها ساخته شود
    * BaseUserAdmin
        ~ یه کلاس پایه‌س که به ما امکانات پایه ادمین رو میده

- fieldsets
    * تغیین قالب ادمین پنل
"""
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
	# فرمی که قراره با آن کارکنه
	form = UserChangeForm
	# فرم اضافی
	add_form = UserCreationForm

    # فیلدهایی که باید نشون داده بشه
	list_display = ('email', 'phone_number', 'is_admin')
	# کاربرها بر چه اساسی فیلتر بشن
	list_filter = ('is_admin',)
	# چه فیلدی فقط برای خواندن باشه
	readonly_fields = ('last_login',)

    # فیلدست فرم اصلی
	fieldsets = (
		# عنوان و فیلدها
		('Main', {'fields':('email', 'phone_number', 'full_name', 'password')}),
		('Permissions', {'fields':('is_active', 'is_admin', 'is_superuser', 'last_login', 'groups', 'user_permissions')}),
	)

    # فیلدست فرم اضافی
	add_fieldsets = (
		(None, {'fields':('phone_number', 'email', 'full_name', 'password1', 'password2')}),
	)

    # سرچ کردن با کدوم فیلد انجام بشه
	search_fields = ('email', 'full_name')
	# اوردر کردن براساس
	ordering = ('full_name',)
	# دوتا مقدار رو کنار هم میذاره
    # واسه پرمیشن‌ها بکار میره
	filter_horizontal = ('groups', 'user_permissions')

	def get_form(self, request, obj=None, **kwargs):
		form = super().get_form(request, obj, **kwargs)
		is_superuser = request.user.is_superuser
		if not is_superuser:
			form.base_fields['is_superuser'].disabled = True
		return form


# رجیستر کردن مدل یوزر با فرم کاستوم
admin.site.register(User, UserAdmin)
