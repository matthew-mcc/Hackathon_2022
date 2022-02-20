from django.shortcuts import render
from django.template import loader

def geeks_view(request):
    # create a dictionary
    context = {
        "first_name" : "Naveen",
        "last_name"  : "Arora",
    }
    # return response
    return render(request, "home.html", context)

def test1(request):
    context = {
        "first_name" : "kev",
        "last_name"  : "v",
    }
    return render(request, "home.html", context)
    
def test2(request):
    context = {
        "first_name" : "kenny",
        "last_name"  : "j",
    }
    return render(request, "home.html", context)