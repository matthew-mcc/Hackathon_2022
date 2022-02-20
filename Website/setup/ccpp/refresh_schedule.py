from Scheduling.schedulingFinal import get_ride_order
from Database.database import database_to_dict, update_group_id, change_drivers

# Change the drivers right before alg is ran
change_drivers()

# retrieve drivers and non drivers
group_drivers_dict, non_drivers_dict = database_to_dict()

wp = {
    "UniversityOfCalgary": "2500 University Dr NW, Calgary"}

# run algo
group_list, location_data = get_ride_order(group_drivers_dict, non_drivers_dict, wp)

# Update the database
count = 0
for k, v in group_list.items():
    for i in v:
        update_group_id(i, count)
    update_group_id(k, count)
    count += 1 
