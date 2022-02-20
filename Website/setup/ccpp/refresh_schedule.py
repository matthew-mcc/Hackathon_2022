from Scheduling.schedulingFinal import get_ride_order
from Database.database import database_to_dict, update_group_id, change_drivers


change_drivers()
group_drivers_dict, non_drivers_dict = database_to_dict()

wp = {
    "UniversityOfCalgary": "2500 University Dr NW, Calgary"}
group_list, location_data = get_ride_order(group_drivers_dict, non_drivers_dict, wp)
