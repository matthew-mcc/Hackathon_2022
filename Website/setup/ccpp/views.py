from django.shortcuts import render
from django.template import loader
from Scheduling.schedulingFinal import get_ride_order
from Database.database import database_to_dict, update_group_id, change_drivers

def geeks_view(request):
    # create a dictionary
    context = {
        "first_name" : "Naveen",
        "last_name"  : "Arora",
    }
    # return response
    return render(request, "home.html", context)

def refresh_schedule(request):
    # Change the drivers right before alg is ran
    # change_drivers()

    # # retrieve drivers and non drivers
    # group_drivers_dict, non_drivers_dict = database_to_dict()

    # wp = {
    #     "UniversityOfCalgary": "2500 University Dr NW, Calgary"}

    # # run algo
    # group_list, location_data = get_ride_order(group_drivers_dict, non_drivers_dict, wp)

    # # Update the database
    # count = 0
    # for k, v in group_list.items():
    #     for i in v:
    #         update_group_id(i, count)
    #     update_group_id(k, count)
    #     count += 1 
    print("Refresh is working")

    return render(request, "home.html")


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