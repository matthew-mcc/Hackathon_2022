from pickle import NONE
from django.shortcuts import render
from django.template import loader

def geeks_view(request):
    # create a dictionary
    context = {}
    mylist = [] 
    mylist.append("hello")
    mylist.append("my")
    mylist.append("name")
    mylist.append("is Ken")
    context['my_list'] = mylist
    # return response
    return render(request, "home.html", context)
