import sys
sys.path.append(R"C:\Users\vanes\eclipse-workspace\ENSF480FinalProject\src\Hackathon_2022")
from schedulingFinal import get_ride_order
from Database.database import database_to_dict, update_group_id



group_drivers_dict, non_drivers_dict = database_to_dict()

wp = {
    "UniversityOfCalgary": "2500 University Dr NW, Calgary"}
group_list, location_data = get_ride_order(group_drivers_dict, non_drivers_dict, wp)

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