from pickle import NONE
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

from django.template.loader import render_to_string



# Create your views here.
# def default_map(request):
#     # TODO: move this token to Django settings from an environment variable
#     # found in the Mapbox account settings and getting started instructions
#     # see https://www.mapbox.com/account/ under the "Access tokens" section
#     mapbox_access_token = 'pk.my_mapbox_access_token'
#     return render(request, 'default.html', 
#                   { 'mapbox_access_token': mapbox_access_token })
students = [
    {'test': 'test1'}
]

def test_data(request):
    
    return render(request, 'home.html', {'stds':students})