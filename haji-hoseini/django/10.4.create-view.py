# olternative of modelforms

# 0
# open "appname/views.py"

# 1
# نوشتن کد زیر
from django.views import generic
from .models import DatabaseName


class BookCreateView(generic.CreateView):
    model = DatabaseName
    fields = ['title', 'content', 'author', 'price', 'status']
    template_name = 'appname\index.html'

# 2
# html form
# نوشتن کد زیر پدر تمپلیت مورد نظر
# حالت اول
"""
<form method="POST">
    {% csrf_token %}
    {{ form }}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
"""
