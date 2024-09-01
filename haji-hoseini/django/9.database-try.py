
"""style 1"""
from django.shortcuts import render
from .models import database_name

def response_def_with_input(request, input_name) :
    try :
        target_data = database_name.objects.get(pk=input_name)
    except database_name.DoesNotExist :
        target_data = None
        print('exceped!')
    return render(request, "appname\index.html", {'data': target_data})

"""style 2"""
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import database_name

def response_def_with_input(request, input_name) :
    try :
        target_data = database_name.objects.get(pk=input_name)
    except ObjectDoesNotExist :
        target_data = None
        print('exceped!')
    return render(request, "appname\index.html", {'data': target_data})

"""style 3"""
from django.shortcuts import render, get_object_or_404
from .models import database_name

def response_def_with_input(request, input_name) :
    target_data = get_object_or_404(database_name, pk=input_name)
    return render(request, "appname\index.html", {'data': target_data})
