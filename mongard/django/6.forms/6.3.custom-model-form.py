"""

- widget:
    * باهاش میتونیم رفتار فرم هامون رو تغییر بدیم

- placeholder:
    * داخل اینپوتمون چی قرار بگیره؟


"""

# 0
# create and open this file "./[app_name]/forms.py" and write bellow code

from django import forms
from .models import ModelName


class NewModelNameForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={})
    )
    password = forms.PasswordInput(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
                'placeholder': 'your password'
            }
        )
    )
    comment = forms.CharField(
        widget=forms.Textarea,
    )


