import pandas as pd

employees_df = pd.read_csv("employees.csv")

drivers = employees_df[employees_df["Carpool_Driver"] == 1]

names_address_dict = dict(zip(
    employees_df.First_Name + " " + employees_df.Last_Name, 
    employees_df.Address))

print(drivers)
print(names_address_dict)