import pandas as pd

employees_df = pd.read_csv("employees.csv")

names_address_dict = dict(zip(
    employees_df.First_Name + " " + employees_df.Last_Name, 
    employees_df.Address))
