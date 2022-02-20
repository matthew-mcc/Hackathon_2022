import pandas as pd

employees_df = pd.read_csv("employees.csv", index_col="Employee_ID")
group_df = pd.read_csv("carpool_groups.csv", index_col="fk_Employee_ID")
drivers_df = pd.read_csv("driver.csv", index_col="Driver_ID")

group_drivers_df = employees_df[group_df["Group_Driver"] == 1].join(drivers_df, on="Driver_ID")
group_drivers_df

print(group_drivers_df)

# group_drivers_dict = dict(zip(
#     group_drivers_df.First_Name + "_" + group_drivers_df.Last_Name,

# ))
