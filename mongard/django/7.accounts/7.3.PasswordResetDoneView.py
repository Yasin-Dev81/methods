"""

"""

# 1
# open "./accounts/views.py" and write bellow code
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
	template_name = 'accounts/password_reset_done.html'

# 2
# open "./accounts/urls.py" and add this path
from django.urls import path

urlpatterns = [
    path('reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
]

# 3
# create "./accounts/templates/accounts/password_reset_done.html" and write bellow code
"""
{% extends '_base.html' %}

{% block content %}
  <p>we sent you an email.</p>
{% endblock %}

"""
