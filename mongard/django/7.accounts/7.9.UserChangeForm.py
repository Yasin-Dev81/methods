"""
- در جنگو میتوانیم برای فرم تغییر اطلاعات کاربر پسورد را هش و غیرقابل تغییر نشان دهیم

"""
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField(help_text="you can change password using <a href=\"../password/\">this form</a>.")

	class Meta:
		model = User
		fields = ('email', 'phone_number', 'full_name', 'password', 'last_login')
