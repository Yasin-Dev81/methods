"""

"""

# 1
# write class in "./app_name/views.py"
from django.http import HttpResponse
from django.views import View


class MyView(View):

    # for get request
    def get(self, request):
        return HttpResponse('Hello, World')

    # for post request
    def post(self, request):
        pass


# 2
# add path of class in urls
from django.urls import path
# from app_name.views import MyView


urlpatterns = [
    path('.../', MyView.as_view(), name='...')
]

