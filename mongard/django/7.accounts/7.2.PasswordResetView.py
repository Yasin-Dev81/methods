"""

"""

# 1
# open "./accounts/views.py" and write bellow code
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'


# 2
# open "./accounts/urls.py" and add this path
from django.urls import path

urlpatterns = [
    path('reset/', UserPasswordResetView.as_view(), name='reset_password'),
]

# 3
# create "./accounts/templates/accounts/password_reset_form.html" and write bellow code
"""
{% extends '_base.html' %}

{% block content %}
    <form action="" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Send">
    </form>
{% endblock %}

"""

# 4
# create "./accounts/templates/accounts/password_reset_email.html" and write bellow code
"""
Someone asked for password reset for email {{ email }}. Follow the link below:

{{ protocol}}://{{ domain }}{% url 'accounts:password_reset_confirm' uidb64=uid token=token %}
"""
