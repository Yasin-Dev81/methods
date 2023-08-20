"""

- View Method Flowchart: به ترتیب اجرا شدنشون
    * setup()
        ~ اطلاعاتی که قراره داخل همه متدها استفاده بشه رو داخل خودش ذخیره میکنه
        ~ برای بهینه تر شدن کد
    * dispatch()
        ~ متدی که قبل از بقیه متدها اجرا میشه
    * http_method_not_allowed()
    * options()


"""
# ex dispatch
from django.views import generic
from django.shortcuts import redirect

class SampleView(generic.View):

    def dispatch(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        if not request.user.is_authenticated:
            # اضافه کردن آرگومان به متد ها
            kwargs['ananimus'] = True
        return super().dispatch(request, *args, **kwargs)
