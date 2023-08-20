"""
- برای چک کردن مقادیر ورودی داخل یه فرم


"""
# ex 1
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    # اعتبارسنجی یه فیلد
	def clean_email(self):
		email = self.cleaned_data['email']
		user = User.objects.filter(email=email).exists()
		if user:
			raise ValidationError('this email already exists')
		return email

    # اعتبارسنجی دو فیلد نسبت به هم
	def clean(self):
		cd = super().clean()
		p1 = cd.get('password1')
		p2 = cd.get('password2')

		if p1 and p2 and p1 != p2:
			raise ValidationError('password must match')
		

# ex 2
class PostCreateUpdateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body', )
	
    def clean_title(self):
        title = self.cleaned_data['title']
        if User.objects.filter(title=title).exists():
            raise ValidationError('this title already exists')
        return title
