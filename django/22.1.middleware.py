"برای ثبت لاگ ها وب سایت به کار می رود"

# 1
# create app "demo_middleware" and add to "./config/settings.py"
"python manage.py startapp demo_middleware"
"docker-compose exec web python manage.py startapp demo_middleware"

INSTALLED_APPS = [
    '...',
    'demo_middleware',
]

MIDDLEWARE = [
    '...',
    # optional
    'demo_middleware.middleware.DemoMiddleware',
]

# 2
# create file "./demo_middleware/middleware.py" and write bellow code
from django.db.models import F
from .models import NewStats


class DemoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.num_request = 0
        self.num_exceptions = 0
        self.context_response = {
            "msg": {
                "warning": "There is no more ink in the printer."
            }
        }

    def __call__(self, request):
        if "admin" not in request.path:
            self.num_request += 1
            print('---No. of request:', self.num_request)

            self.stats(request.META['HTTP_USER_AGENT'])

        response = self.get_response(request)
        return response

    # for request
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('---view name [def/class]: %s' % view_func.__name__)

    def process_request(self, request):
        pass

    # for response
    def process_exception(self, request, exception):
        self.num_exceptions += 1
        print('---Exception count:', self.num_exceptions)
        print('---this exception:', exception)

    def process_response(self, request, response):
        pass

    def process_template_response(self, request, response):
        self.context_response["new_data"] = self.context_response
        return response

    # extra
    def stats(self, os_info):
        if "Windows" in os_info:
            NewStats.objects.all().update(win=F('win') + 1)
        elif "mac" in os_info:
            NewStats.objects.all().update(win=F('mac') + 1)
        elif "iPhone" in os_info:
            NewStats.objects.all().update(win=F('iph') + 1)
        elif "Android" in os_info:
            NewStats.objects.all().update(win=F('android') + 1)
        else:
            NewStats.objects.all().update(win=F('oth') + 1)


class DemoException(Exception):  # rise in view def
    pass


# 3
# write this code in "./demo_middleware/models.py"
from django.db import models


class NewStats(models.Model):
    win = models.IntegerField()
    mac = models.IntegerField()
    iph = models.IntegerField()
    android = models.IntegerField()
    oth = models.IntegerField()


# 4
# write this code in "./demo_middleware/admin.py"
from django.contrib import admin

from .models import NewStats


@admin.register(NewStats)
class NewStatsAdmin(admin.ModelAdmin):
    pass



# 5
# create file "./templates/admin/demo_middleware/newstats/change_list.html" and write this code
"""

"""