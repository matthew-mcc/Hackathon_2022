
input_data = {
    "Driver": "379 Springborough Way SW, Calgary",
    "Workplace": "2500 University Dr NW, Calgary",
    "John": "198 Cougar Plateau Way SW, Calgary",
    "Jane": "147 Prominence Heights SW, Calgary",
    "Josh": "317 Wentworth Place SW, Calgary",
    "Matthew": "70 Elkton Way SW, Calgary",
    "Kevin": "187 Tremblant Way SW, Calgary",
    "Tus": "25 Wentworth Terrace SW, Calgary"
}

def get_ride_order(input_data):
    # converting data to lat-lon
    from geopy.geocoders import Nominatim
    import geopy.distance


    geolocater = Nominatim(user_agent="My Application")

    lat_lon_data = {}
    for key in input_data:
    
        location = geolocater.geocode(input_data[key])
        try:
            tup = (location.raw["lat"], location.raw["lon"])
            lat_lon_data[key] = tup
        except Exception as e:
            print("Weird Error At the end of dic")
            # NOT SEEING TUS BUT W H Y



    driver_loc = lat_lon_data["Driver"]
    workplace_loc = lat_lon_data["Workplace"]

    del lat_lon_data["Driver"]
    del lat_lon_data["Workplace"]
    


    # now that we have all of the data sorted for lat long we need to find the closest n people to the driver.
    distance_to_driver = {}
    # geopy.distance.distance(coord1, coord2).km

    for key in lat_lon_data:
        my_tup = lat_lon_data[key]
        distance = geopy.distance.distance(driver_loc, lat_lon_data[key]).km
        distance_to_driver[key] = distance

    distance_to_workplace = {}

    n = int(input("How many people can you pick up: "))
    all_driver_distances = list(distance_to_driver.values())

    index_driver_list = sorted(range(len(all_driver_distances)), key = lambda sub: all_driver_distances[sub])[:n]

    # we now need a list of the peeps that will be going in the carpool

    carpool = []
    key_list = list(distance_to_driver)

    for ele in index_driver_list:
        carpool.append(key_list[ele])

      # stores the names of the closest n people


    distance_to_workplace = {}
    for key in lat_lon_data:
        my_tup = lat_lon_data[key]
        distance = geopy.distance.distance(workplace_loc, lat_lon_data[key]).km
        distance_to_workplace[key] = distance



    distance_to_workplace_carpool = {}
    for ele in carpool:
        distance_to_workplace_carpool[ele] = distance_to_workplace[ele]



    ride_order = []
    all_workplace_distances_carpool = list(distance_to_workplace_carpool.values())

    import numpy as np
    index_ride_order = np.array(all_workplace_distances_carpool).argsort().tolist()[::-1]


    key_list_workplace = list(distance_to_workplace_carpool)
    for ele in index_ride_order:
        ride_order.append(key_list_workplace[ele])

    return(ride_order)


print("Ride Order: ",get_ride_order(input_data))