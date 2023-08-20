"""
"""

# 1
# open "./accounts/views.py" and write bellow code
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
	template_name = 'accounts/password_reset_confirm.html'
	success_url = reverse_lazy('accounts:password_reset_complete')

# 2
# open "./accounts/urls.py" and add this path
from django.urls import path

urlpatterns = [
    path('confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

# 3
# create "./accounts/templates/accounts/password_reset_confirm.html" and write bellow code
"""
{% extends '_base.html' %}

{% block content %}
    {% if validlink %}
        <form action="" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Change">
        </form>
    {% else %}
        <p>this link is not valid. please try again.</p>
    {% endif %}
{% endblock %}
"""
