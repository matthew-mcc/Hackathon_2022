from schedulingFinal import get_ride_order

import pandas as pd

employees_df = pd.read_csv("employees.csv", index_col="Employee_ID")
group_df = pd.read_csv("carpool_groups.csv", index_col="fk_Employee_ID")
drivers_df = pd.read_csv("driver.csv", index_col="Driver_ID")

group_drivers_df = employees_df[group_df["Group_Driver"] == 1].join(drivers_df, on="Driver_ID")

group_drivers_dict = {}
for idx, item in group_drivers_df.iterrows():
    address_and_max_seats = (item["Address"] + ", " + item["City"], item["Max_Seats"])
    full_name = item["First_Name"] + "_" + item["Last_Name"]
    group_drivers_dict[full_name] = address_and_max_seats


non_drivers_df = employees_df[group_df["Group_Driver"] == 0]
non_drivers_dict = dict(zip(
    non_drivers_df.First_Name + "_" + non_drivers_df.Last_Name,
    non_drivers_df.Address + ", " + non_drivers_df.City))

group_list, location_data = get_ride_order(group_drivers_dict, non_drivers_dict, workplace_data = {
    "UniversityOfCalgary": "2500 University Dr NW, Calgary"})




for keys, values in groups_list.items():
    print(keys, "drives", values)


print("The location of each individual in Lat-Lon is:")
for key in location_data:
    print(key, location_data[key])