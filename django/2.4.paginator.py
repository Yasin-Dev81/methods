# paginator

"""in class based"""

# views.py:
from django.views import generic
from .models import DataBaseName

class NameListView(generic.ListView):
    model = DataBaseName
    paginate_by = 4
    template_name = '[appname]/index.html'
    context_object_name = 'books'

# index.html
"""
    <nav aria-label="...">
        <ul class="pagination">
            {% if page_obj.has_previous %}
                <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}">{{ page_obj.previous_page_number }} (Previous)</a></li>
            {% endif %}
            <li class="page-item active">
                <span class="page-link">
                {{ page_obj.number }}
                <span class="sr-only">(current)</span>
                </span>
            </li>
            {% if page_obj.has_next %}
                <li class="page-item"><a class="page-link" href="?page={{ page_obj.next_page_number }}">{{ page_obj.next_page_number }} (Next)</a></li>
            {% endif %}
        </ul>
    </nav>
"""

# --------------------------------------

"""in function based"""

from django.shortcuts import render
from .models import DataBaseName
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def name_list_view(request):
    writer_list = DataBaseName.objects.all()
    page = request.GET.get('page', 1)

    paginate_by = 4
    paginator = Paginator(writer_list, paginate_by)

    try:
        values = paginator.page(page)
    except PageNotAnInteger:
        values = paginator.page(1)
    except EmptyPage:
        values = paginator.page(paginator.num_pages)

    return render(request, '[app-name]/index.html', context={'values': values})


# in index.html
"""
    <nav aria-label="...">
        <ul class="pagination">
            {% if values.has_previous %}
                <li class="page-item"><a class="page-link"
                                         href="?page={{ values.previous_page_number }}">{{ values.previous_page_number }}
                    (Previous)</a></li>
            {% endif %}
            <li class="page-item active">
                <span class="page-link">
                {{ values.number }}
                <span class="sr-only">(current)</span>
                </span>
            </li>
            {% if values.has_next %}
                <li class="page-item">
                    <a class="page-link"
                       href="?page={{ values.next_page_number }}">{{ values.next_page_number }}
                        (Next)</a></li>
            {% endif %}
        </ul>
    </nav>
"""
