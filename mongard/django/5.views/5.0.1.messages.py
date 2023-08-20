"""

- سطوح مسیج‌ها:
    * 
"""

from django.contrib import messages


def ex_view(request):
    '...'

    # روش یک
    messages.add_message(request, messages.INFO, '...', extra_tags='info')
    
    # روش دو
    messages.info(request, '...', extra_tags='info')
    '...'
