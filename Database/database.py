import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="vanessa",
  password="vanessa",
  database='car_pool_planner'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employee")

myresult = mycursor.fetchall()

employee_df = pd.read_sql("SELECT * FROM employee", con=mydb, index_col="Employee_ID")
carpool_groups_df = pd.read_sql("SELECT * FROM carpool_groups", con=mydb, index_col="fk_Employee_ID")
driver_df = pd.read_sql("SELECT * FROM driver", con=mydb, index_col="Driver_ID")
company_df = pd.read_sql("SELECT * FROM company", con=mydb, index_col="Company_ID")

# Get dictionary of those chosen to drive the groups
group_drivers_df = employee_df[carpool_groups_df["Group_Driver"] == 1].join(carpool_groups_df, on="Driver_ID")

group_drivers_dict = {}

for idx, item in group_drivers_df.iterrows():
    address_and_max_seats = (item["Address"] + ", " + item["City"], item["Max_Seats"])
    full_name = item["First_Name"] + "_" + item["Last_Name"]
    group_drivers_dict[full_name] = address_and_max_seats

# Get dictionary of those who were not chosen to drive
non_drivers_df = employee_df[carpool_groups_df["Group_Driver"] == 0]
non_drivers_dict = dict(zip(
    non_drivers_df.First_Name + "_" + non_drivers_df.Last_Name,
    non_drivers_df.Address + ", " + non_drivers_df.City))

employee_df.to_csv("employees.csv")
carpool_groups_df.to_csv("carpool_groups.csv")
driver_df.to_csv("driver.csv")
company_df.to_csv("company.csv")
