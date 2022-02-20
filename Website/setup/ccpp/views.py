from pickle import NONE
from django.shortcuts import render
from django.template import loader

# Create your views here.
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'default.html', 
                  { 'mapbox_access_token': mapbox_access_token })


def send_data(request):
    context = {}
    context['somestring'] = "this is some string"

    return render(request, "home.html", context)