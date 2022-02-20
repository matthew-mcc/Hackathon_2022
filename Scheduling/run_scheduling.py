from schedulingFinal import get_ride_order
from Database.database import database_to_dic



group_drivers_dict, non_drivers_dict = database_to_dic()

wp = {
    "UniversityOfCalgary": "2500 University Dr NW, Calgary"}
group_list, location_data = get_ride_order(group_drivers_dict, non_drivers_dict, wp)




for keys, values in group_list.items():
    print(keys, "drives", values)


print("The location of each individual in Lat-Lon is:")
for key in location_data:
    print(key, location_data[key])