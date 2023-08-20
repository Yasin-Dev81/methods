# ModelForm: 
# ساخت یک فرم در دیتابیس برای ذخیره سازی بهتر اطلاعات در ویو

# 1
# ساخت فایل زیر و بازکردن آن
# create and open this file: 
"[app-name]/forms.py"

# 2
# نوشتن کد زیر
from django.forms import ModelForm
from .models import DatabaseName


class NewDatabaseNameForm(ModelForm):
    class Meta:
        model = DatabaseName
        fields = ['sotoon_name1', 'sotoon_name2', 'author'] # مادل های مورد نیاز


# 3
# استایل کد در ویو

from .forms import NewDatabaseNameForm

def response_def(request) : # تابع ریسپانس با اسم دلخواه
    if request.method == 'POST':
        # add data in data-base with forms
        new_formname_form = NewDatabaseNameForm(request.POST)
        if new_formname_form.is_valid():
            new_formname_form.save()  # save data
            formname_form = NewDatabaseNameForm() # for cleaned page(template)
        else:
            formname_form = NewDatabaseNameForm()
    else:
        formname_form = NewDatabaseNameForm() # send forms to templates
    return render(request, "appname\index.html", context={'new_database_form': formname_form})

# ***
# Redirect
# فرستادن فرد به صفحه دیگری از وب
"""redirect('[url-name]')"""
from django.shortcuts import render, redirect

def response_def(request):  # تابع ریسپانس با اسم دلخواه
    if request.method == 'POST':
        # add data in data-base with forms
        new_formname_form = NewDatabaseNameForm(request.POST)
        if new_formname_form.is_valid():
            new_formname = new_formname_form.save(commit=False)
            # مقادیری که می خواهیم خودمان وارد کنیم
            new_formname.book = 'book'
            new_formname.username = request.user
            new_formname.save()
            return redirect(reverse('[url-name]'))
        else:
            formname_form = NewDatabaseNameForm()
    else:
        formname_form = NewDatabaseNameForm()  # send forms to templates
    return render(request, "appname\index.html", context={'new_database_form': formname_form})

# ****
# update data
# ex:
from django.shortcuts import get_object_or_404
def update_blog_response(request, blog_id):
    blog_post = get_object_or_404(DatabaseName, pk=blog_id)
    print(blog_post)
    blogpost_form = NewDatabaseNameForm(request.POST or None, instance=blog_post)
    if blogpost_form.is_valid():
        blogpost_form.save()
        return redirect('blog_detail_url', blog_post.pk, blog_post.title)
    else:
        blogpost_form = NewDatabaseNameForm(request.POST or None, instance=blog_post)
    return render(request, 'blog/add_blog.html', context={'new_blogpost_form': blogpost_form})


# 4
# نوشتن کد زیر پدر تمپلیت مورد نظر
# حالت اول
"""
<form method="POST">
    {% csrf_token %}
    {{ new_blogpost_form.as_p }} {# <p> form </p> #}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
"""
# حالت دوم
"""
<form method="POST">
    {% csrf_token %}
    <table>
        {{ new_blogpost_form.as_table }} 
    </table>
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
"""
# حالت دوم
"""
<form method="POST">
    {% csrf_token %}
    <ul>
        {{ new_blogpost_form.as_ul }} 
    </ul>
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
"""
