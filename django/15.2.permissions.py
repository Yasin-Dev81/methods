# authorization(permissions): برای سطح دسترسی
# authentication: شما کی هستید؟

"class base"

# ex:
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import DataBaseName

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = DataBaseName
    fields = ['title', 'content', 'price', 'status', 'cover']
    template_name = 'books/update_book.html'

    def test_func(self):
        return self.get_object().user == self.request.user


class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = DataBaseName
    fields = ['title', 'content', 'author', 'price', 'status', 'cover']
    template_name = 'books/create_book.html'

    def test_func(self):
        return self.request.user.is_staff


"functional base"
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def view():
    pass
