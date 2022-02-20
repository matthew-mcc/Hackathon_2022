






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
    #print(passenger_latLon)
    for driver in driver_latLon:
        # calculate distance from all CURRENT passengers, to the current driver
        distance_to_current_driver = {}

        for key in passenger_latLon:
            distance = geopy.distance.distance(driver_latLon[driver], passenger_latLon[key]).km
            distance_to_current_driver[key] = distance

       # print(distance_to_current_driver)
        N = driver_seats[driver]
       # group = dict(sorted(distance_to_current_driver.items(), key=itemgetter(1), reverse=True)[:N])
        group = nsmallest(N, distance_to_current_driver, key = distance_to_current_driver.get)
        #print(N)
        #print("Passengers")
       # print(distance_to_current_driver)
       # print("Group Selected")
       # print(group)
        driver_and_group = {driver: group}
        group_list.append(driver_and_group)

        #now remove everything that has been added(FROM latlon)
        del input_dataDriver[driver]
        for ele in group:
            del passenger_latLon[ele]


    #group list stores a list of dicts with {driver: [passengers]}
   # print("Group List")
   # print(group_list)
  #  print(input_dataDriver) 
  #  print(passenger_latLon) #remaining passengers that didn't get a ride
   # print(passenger_data_for_workplace) #latlon to calculate distance of workspace

    distance_to_workplace = {}
    for key in passenger_data_for_workplace:
        distance = geopy.distance.distance()
    
    passenger_distances = []
    for group in group_list:
        passenger_list = (group.values())
        #print(group, "group")
        
        passenger_distance_to_workplace = {}
        for passenger in passenger_list:
            for curr_pass in passenger:
                #print("passenger", curr_pass)
                dist = geopy.distance.distance(workplace_location, passenger_data_for_workplace[curr_pass]).km
                passenger_distance_to_workplace[curr_pass] = dist
            passenger_distances.append(passenger_distance_to_workplace)
    
   # print(passenger_distances)
    

    #need to sort passenger_distances to get ORDER,
    route_order = []
    for ele in passenger_distances:
        route_dict = sorted(ele.items(), key=itemgetter(1), reverse=True)
        route_order.append(route_dict)

    #print("route order", route_order)

    

    final_groups = []
    for group in route_order:
        new_group = []
        for person in group:
            new_group.append(person[0])

        
        
        final_groups.append(new_group)
            #driver_and_group[driver] = new_group
 #   print("Driver and group", group_list, "\n") 
 #   print("route order", route_order)
  #  print("final groups", final_groups)


    
    driver_list = []
    for group in group_list:
        for driver in group:
           # print("driver", driver)
            driver_list.append(driver)
    
  #  print("driver list", driver_list)
  #  print("final_groups", final_groups)
    #for group in final_groups:
    output_dictionary = dict(zip(driver_list, final_groups))
   # print(output_dictionary)

    all_latLon = {**passenger_data_for_workplace, **driver_latLon}

    return output_dictionary, all_latLon

            
    #print("final order", driver_and_group)
    
    #then put back w respective driver...

        #pick the closest passengers, add them to a group 





# driver_data = {
#     "Jimbo": ("379 Springborough Way SW, Calgary", 4),
#     "Bimbo": ("198 Cougar Plateau Way SW, Calgary", 3),
#     "Dimbo": ("147 Prominence Heights SW, Calgary", 2),

# }

# passenger_data = {
#     "Josh": "317 Wentworth Place SW, Calgary",
#     "Matthew": "70 Elkton Way SW, Calgary",
#     "Kevin": "187 Tremblant Way SW, Calgary",
#     "Tus": "25 Wentworth Terrace SW, Calgary",
#     "Gus": "114 Warwick Drive SW, Calgary",
#     "Kenny": "315 Coach Ride Rise SW, Calgary",
#     "Nate": "417 Patina Pl SW, Calgary",
#     "Erwin": "843 77 Street SW, Calgary",
#     "Brendan": "135 Discovery Ridge Way SW, Calgary",

# }

# workplace_data = {
#     "UniversityOfCalgary": "2500 University Dr NW, Calgary",
# }

# groups, data = get_ride_order(driver_data, passenger_data, workplace_data)


# for keys, values in groups.items():
#     print(keys, "drives", values)


# print("The location of each individual in Lat-Lon is:")
# for key in data:
#     print(key, data[key])