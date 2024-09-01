
# 
# 1) functional view -> view def
# 2) class-based view

# 1)
from pyexpat import model
from django.shortcuts import render

def response_def(request) : # تابع ریسپانس با اسم دلخواه
    context_dictionary = {
        "Variable": "somthing",
    }
    return render(request, "appname\index.html", context_dictionary)

# 2)

from django.views import generic # generic view # ویو های جنرال


class Response_class(generic.somthing):
    pass

# ex:
# views.py
from .models import BlogPost

# ex for all:
class PostListView(generic.ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog_list'

# ex for filter and else
class PostListView(generic.ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs_list'

    def get_queryset(self):
        return BlogPost.objects.filter(status='pub').order_by('-datetime_edited')


# ex for comment


# urls.py
from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostListView.as_view(), name='somthing-name'),
]

