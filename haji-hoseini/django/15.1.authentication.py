# authentication: شما کی هستید؟
# authorization(permissions): برای سطح دسترسی


"in functional base"

# ex:
from django.shortcuts import reverse, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import DataBaseName

@login_required()
def inactive_comment_view(request, pk):
    if request.user.is_staff:
        comment = get_object_or_404(DataBaseName, pk=pk)
        comment.is_active = False
        comment.save()
        return redirect(reverse('book_detail_url', args=(comment.book.pk, comment.book.title)))
    else:
        return HttpResponse('Access is limited')



"in class base"

# ex:
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DataBaseName

class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DataBaseName
    fields = ['title', 'content', 'price', 'status', 'cover']
    template_name = 'books/update_book.html'

