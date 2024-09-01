

# 1
# add bellow code in "_base.html"
# زیر هدر

# ex 1:
"""
{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
    {% endfor %}
</ul>
{% endif %}
"""
# ex 2:
"""
{% if messages %}
    <div class="container">
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
{% endif %}
"""

# 2
# in views.py:
from django.contrib import messages
from django.shortcuts import render


def ex_view(request):
    messages.success(request, 'This is a success message.')
    return render(request, '...')


# تغییر تگ های مسیج
"./config/settings.py"
# For messages framework
from django.contrib.messages import constants as message_constants

MESSAGE_TAGS = {
    message_constants.ERROR: 'danger',
}
