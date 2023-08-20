"""
- پر کردن فرم با دیتا برای آپدیت ویو
    * with (instance=<data of database>)
- ارسال اطلاعات اضافی
    * with (initial=<data: dict>)

"""
# 0
# create and open this file "./[app_name]/forms.py" and write bellow code

from django.forms import ModelForm
from .models import ModelName

from django import forms
from django.core.exceptions import ValidationError

# type 1
class UserRegistrationForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

	def clean_email(self):
		email = self.cleaned_data['email']
		user = User.objects.filter(email=email).exists()
		if user:
			raise ValidationError('this email already exists')
		return email

	def clean(self):
		cd = super().clean()
		p1 = cd.get('password1')
		p2 = cd.get('password2')

		if p1 and p2 and p1 != p2:
			raise ValidationError('password must match')

# type 2
class EditUserForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = Profile
		fields = ('age', 'bio')


# 1
# open "./[app_name]/views.py" and write bellow code

# ***
# برای ساخت دیتا
# functional-based
from django.shortcuts import render, redirect

def response_def(request):  # تابع ریسپانس با اسم دلخواه
    if request.method == 'POST':
        # add data in data-base with forms
        new_formname_form = NewModelNameForm(request.POST)
        if new_formname_form.is_valid():
            new_formname = new_formname_form.save(commit=False)
            # مقادیری که می خواهیم خودمان وارد کنیم
            new_formname.book = 'book'
            new_formname.username = request.user
            new_formname.save()
            return redirect(reverse('[url_name]'))
        else:
            formname_form = NewModelNameForm()
    else:
        formname_form = NewModelNameForm()  # send forms to templates
    # return form
    return render(
        request, 
        "appname\index.html", 
        context={
            'model_form': formname_form,
        }
    )

# class-based
from django.views import View

class ResponseView(View):
    form_class = NewModelNameForm

    template_name = "appname\index.html"

    def get(self, request):
        return render(
            request, 
            template_name=self.template_name, 
            context={
                'model_form': self.form_class(),
            }
        )

    def post(self, request):
        # add data in data-base with forms
        new_formname_form = self.form_class(request.POST)
        if new_formname_form.is_valid():
            new_formname = new_formname_form.save(commit=False)
            # مقادیری که می خواهیم خودمان وارد کنیم
            new_formname.book = 'book'
            new_formname.username = request.user
            new_formname.save()
            return redirect(reverse('[url_name]'))
        else:
            return render(
                request, 
                template_name=self.template_name, 
                context={
                    'model_form': self.form_class(),
                }
            )


# ****
# آپدیت یا ادیت دیتا
# ex:
from django.shortcuts import get_object_or_404
def update_blog_response(request, blog_id):
    blog_post = get_object_or_404(ModelName, pk=blog_id)
    print(blog_post)
    blogpost_form = NewModelNameForm(request.POST or None, instance=blog_post)
    if blogpost_form.is_valid():
        blogpost_form.save()
        return redirect('blog_detail_url', blog_post.pk, blog_post.title)
    else:
        blogpost_form = NewModelNameForm(request.POST or None, instance=blog_post)
    return render(request, 'blog/add_blog.html', context={'new_blogpost_form': blogpost_form})


# 2
# نوشتن کد زیر پدر تمپلیت مورد نظر
# حالت اول
"""
<form method="POST">
    {% csrf_token %}
    {{ new_blogpost_form.as_p }} {# <p> form </p> #}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
"""
