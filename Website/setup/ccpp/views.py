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
    print("refresh")
    return render(request, "home.html")
