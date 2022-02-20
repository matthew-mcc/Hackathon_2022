import pandas as pd

employees_df = pd.read_csv("employees.csv")

# Gets names and employee ID's of those able to drive
drivers = employees_df[employees_df["Carpool_Driver"] == 1].drop(["Address", "City","Carpool_Driver"], axis=1).set_index("Employee_ID")

# Gets all the names and addresses of employees
names_address_dict = dict(zip(
    employees_df.First_Name + " " + employees_df.Last_Name, 
    employees_df.Address))

