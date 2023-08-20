"""

"""

# 1
# open "./accounts/views.py" and write bellow code
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
	template_name = 'accounts/password_reset_done.html'

# 2
# open "./accounts/urls.py" and add this path
from django.urls import path

urlpatterns = [
    path('confirm/complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# 3
# create "./accounts/templates/accounts/password_reset_complet.html" and write bellow code
"""
{% extends '_base.html' %}

{% block content %}
  <p>your password changed.</p>
{% endblock %}

"""
