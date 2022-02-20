import sys
sys.path.append(R"C:\Users\vanes\eclipse-workspace\ENSF480FinalProject\src\Hackathon_2022")
from Database.database import database_to_dict, update_group_id, change_drivers

def run():
    change_drivers()
    group_drivers_dict, non_drivers_dict = database_to_dict()

    wp = {
        "UniversityOfCalgary": "2500 University Dr NW, Calgary"}
    group_list, passenger_location, location_data = get_ride_order(group_drivers_dict, non_drivers_dict, wp)

    count = 0
    for k, v in group_list.items():
        for i in v:
            update_group_id(i, count)
        update_group_id(k, count)
        count += 1 

    for keys, values in group_list.items():
        print(keys, "drives", values)
    
    print("The location of each individual in Lat-Lon is:")
    for key in location_data:
        print(key, location_data[key])

    return group_list, passenger_location, location_data


def get_ride_order(input_dataDriver, input_dataPassengers, workplaceLocation):
    from geopy.geocoders import Nominatim
    import geopy.distance
    import numpy as np
    from operator import itemgetter
    from heapq import nsmallest
    # convert all location to lat-lon
    geolocater = Nominatim(user_agent="Carpool Scheduler")
    
    #convert Driver Data to Lat-Lon
    driver_latLon = {}
    driver_seats = {}
    for key in input_dataDriver:
        driver_seats[key] = input_dataDriver[key][1]
        
    
    for key in input_dataDriver:
        location = geolocater.geocode(input_dataDriver[key])
        try:
            tup = (location.raw["lat"], location.raw["lon"])
            driver_latLon[key] = tup
        except Exception as e:
            print("Failed the last driver")
    #convert Passenger Dawta to Lat-lon
    passenger_latLon = {}
    for key in input_dataPassengers:
        location = geolocater.geocode(input_dataPassengers[key])
        try:
            tup = (location.raw["lat"], location.raw["lon"])
            passenger_latLon[key] = tup
        except Exception as e:
            print("Failed the last passenger")

    passenger_data_for_workplace = dict(passenger_latLon)
    #convert workplace data to lat lon
    workplace_latLon = {}
    for key in workplaceLocation:
        location = geolocater.geocode(workplaceLocation[key])
        tup = (location.raw["lat"], location.raw["lon"])
        workplace_latLon[key] = tup

    workplace_location = next(iter(workplace_latLon.items()))[1]
    #now go through each driver, fill up their car and delete everything that is in the car includind driver

    group_list = []
    for driver in driver_latLon:
        # calculate distance from all CURRENT passengers, to the current driver
        distance_to_current_driver = {}

        for key in passenger_latLon:
            distance = geopy.distance.distance(driver_latLon[driver], passenger_latLon[key]).km
            distance_to_current_driver[key] = distance

        N = driver_seats[driver]
        group = nsmallest(N, distance_to_current_driver, key = distance_to_current_driver.get)
        driver_and_group = {driver: group}
        group_list.append(driver_and_group)

        #now remove everything that has been added(FROM latlon)
        del input_dataDriver[driver]
        for ele in group:
            del passenger_latLon[ele]

    distance_to_workplace = {}
    for key in passenger_data_for_workplace:
        distance = geopy.distance.distance()
    
    passenger_distances = []
    for group in group_list:
        passenger_list = (group.values())
        
        passenger_distance_to_workplace = {}
        for passenger in passenger_list:
            for curr_pass in passenger:
                dist = geopy.distance.distance(workplace_location, passenger_data_for_workplace[curr_pass]).km
                passenger_distance_to_workplace[curr_pass] = dist
            passenger_distances.append(passenger_distance_to_workplace)    

    #need to sort passenger_distances to get ORDER,
    route_order = []
    for ele in passenger_distances:
        route_dict = sorted(ele.items(), key=itemgetter(1), reverse=True)
        route_order.append(route_dict)
    

    final_groups = []
    for group in route_order:
        new_group = []
        for person in group:
            new_group.append(person[0])
        
        final_groups.append(new_group)

    
    driver_list = []
    for group in group_list:
        for driver in group:
            driver_list.append(driver)

    output_dictionary = dict(zip(driver_list, final_groups))

    all_latLon = {**passenger_data_for_workplace, **driver_latLon}

    return output_dictionary, passenger_data_for_workplace, all_latLon

