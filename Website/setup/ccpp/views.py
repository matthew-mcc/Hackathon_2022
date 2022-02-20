from pickle import NONE
from django.shortcuts import render
from django.template import loader
import json

def geeks_view(request):

    test_group = {0: (4, 9, 5, 1), 3: (8, 2, 10, 7), 6: ()}
    test_dict = {1: ('51.0577096', '-114.17297334799039'), 2: ('51.0240558', '-114.1897918'), 4: ('51.0437765', '-114.2100928'), 5: ('51.0559689', '-114.2065182'), 7: ('51.0469793', '-114.167762'), 8: ('51.039615850000004', '-114.22118365182827'), 9: ('51.0616126', '-114.2159037'), 10: ('51.0429677', '-114.184266'), 0: ('51.0688283', '-114.2073793'), 3: ('51.0353356', '-114.2158614'), 6: ('51.0616126', '-114.2159037')}
    tag_value = {0: 'John Smith 198 Cougar Plateau Way SW', 1: 'Jane Doe 147 Prominence Heights SW', 2: 'Matthew McConnell 70 Elkton Way SW', 3: 'Kevin Van 187 Tremblant Way SW', 4: 'Gus Bravo 154 Aspen Summit Cl SW', 5: 'Vanessa Chen 317 Wentworth Pl SW', 6: 'Kenny Jeon 25 Wentworth Terrace SW', 7: 'Josh McConnell 147 Strathcona Close SW', 8: 'Brendan Arthurs 24 Aspen Hills Close SW', 9: 'Carson Eades 25 Wentworth Terrace SW', 10: 'Max Brown 131 Christie Knoll Point SW'}
    # return response
    group_info = {0: [('John', 'Smith', '198 Cougar Plateau Way SW', 1), ('Jane', 'Doe', '147 Prominence Heights SW', 0), ('Gus', 'Bravo', '154 Aspen Summit Cl SW', 0), ('Vanessa', 'Chen', '317 Wentworth Pl SW', 0), ('Carson', 'Eades', '25 Wentworth Terrace SW', 0)], 1: [('Matthew', 'McConnell', '70 Elkton Way SW', 0), ('Kevin', 'Van', '187 Tremblant Way SW', 1), ('Josh', 'McConnell', '147 Strathcona Close SW', 0), ('Brendan', 'Arthurs', '24 Aspen Hills Close SW', 0), ('Max', 'Brown', '131 Christie Knoll Point SW', 0)], 2: [('Kenny', 'Jeon', '25 Wentworth Terrace SW', 1)]}
    
    return render(request, "home.html", {"test_dict":json.dumps(test_dict), "test_group":json.dumps(test_group), "tag_value":json.dumps(tag_value)})
    return render(request, "home.html", {"test_dict":json.dumps(test_dict), "test_group":json.dumps(test_group), "tag_value":json.dumps(tag_value), "group_info":json.dumps(group_info)})


