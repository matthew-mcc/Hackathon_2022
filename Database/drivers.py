import pandas as pd

employees_df = pd.read_csv("employees.csv")

# Gets names and employee ID's of those able to drive
drivers_df = employees_df[employees_df["Carpool_Driver"] == 0]
drivers_dict = dict(zip(
    drivers_df.First_Name + " " + drivers_df.Last_Name,
    drivers_df.Address, 
    ))

# Gets all the names and addresses of employees
no_drivers_df = employees_df[employees_df["Carpool_Driver"] == 1]
no_drivers_dict = dict(zip(
    no_drivers_df.First_Name + " " + no_drivers_df.Last_Name,
    no_drivers_df.Address,
    ))

print(drivers_dict)
print(no_drivers_dict)