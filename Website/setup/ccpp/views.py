from pickle import NONE
from django.shortcuts import render
from django.template import loader
import json

def geeks_view(request):

    # create a dictionary
    # context = {
    #     "first_name" : "Naveen",
    #     "last_name"  : "Arora",
    # }
    test_group = {0: (4, 9, 5, 1), 3: (8, 2, 10, 7), 6: ()}
    test_dict = {1: ('51.0577096', '-114.17297334799039'), 2: ('51.0240558', '-114.1897918'), 4: ('51.0437765', '-114.2100928'), 5: ('51.0559689', '-114.2065182'), 7: ('51.0469793', '-114.167762'), 8: ('51.039615850000004', '-114.22118365182827'), 9: ('51.0616126', '-114.2159037'), 10: ('51.0429677', '-114.184266'), 0: ('51.0688283', '-114.2073793'), 3: ('51.0353356', '-114.2158614'), 6: ('51.0616126', '-114.2159037')}
    print("test")
    # return response
    
    return render(request, "home.html", {"test_dict":json.dumps(test_dict), "test_group":json.dumps(test_group)})