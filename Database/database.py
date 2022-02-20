import mysql.connector
import pandas as pd
from mysql.connector import Error
from string import Template

def database_to_dic():
  mydb = mysql.connector.connect(
    host="localhost",
    user="vanessa",
    password="vanessa",
    database='car_pool_planner'
  )

  mycursor = mydb.cursor()

  employee_df = pd.read_sql("SELECT * FROM employee", con=mydb, )
  carpool_groups_df = pd.read_sql("SELECT * FROM carpool_groups", con=mydb)
  driver_df = pd.read_sql("SELECT * FROM driver", con=mydb)
  company_df = pd.read_sql("SELECT * FROM company", con=mydb)

  # employee_df.to_csv("employees.csv")
  # carpool_groups_df.to_csv("carpool_groups.csv")
  # driver_df.to_csv("driver.csv")
  # company_df.to_csv("company.csv")

  # Get dictionary of those chosen to drive the groups
  can_driver_df = employee_df[carpool_groups_df["Group_Driver"] == 1]
  group_drivers_df = pd.merge(can_driver_df, driver_df, left_on="Employee_ID", right_on="fk_Employee_ID")
  group_drivers_dict = {}

  for idx, item in group_drivers_df.iterrows():
      address_and_max_seats = (item["Address"] + ", " + item["City"], item["Max_Seats"])
      group_drivers_dict[item["Employee_ID"]] = address_and_max_seats

  # Get dictionary of those who were not chosen to drive
  non_drivers_df = employee_df[carpool_groups_df["Group_Driver"] == 0]
  non_drivers_dict = dict(zip(
      non_drivers_df.index,
      non_drivers_df.Address + ", " + non_drivers_df.City))
  return group_drivers_dict, non_drivers_dict



def insert_employee_db(id, fname, lname, address, city, password, max_seats):
    mydb = mysql.connector.connect(
      host="localhost",
      user="vanessa",
      password="vanessa",
      database='car_pool_planner'
    )

    # Employee Table Query
    employee_query_template = Template(
            """INSERT INTO employee
            VALUES($id, \"$fname\", \"$lname\", \"$address\", \"$city\", $drive, \"$password\", $admin, $driver_id, $rides, $drives, $rank)"""
    )
    employee_query = employee_query_template.substitute(
      id=id,
      fname=fname,
      lname=lname,
      address=address,
      city=city,
      password=password,
      admin=0,
      rides=0,
      drives=0,
      rank=0)

    # Driver Query
    driver_query_template = Template(
            """INSERT INTO driver
            VALUES($id, $max_seats, $max_distance_km"""
    )
    driver_query = driver_query_template.substitute(
      id=id,
      max_seats=max_seats,
      max_distance_km=10
    )

    # Carpool Query
    carpool_query_template = Template(
              """INSERT INTO carpool_groups
              VALUES($id, $groupID, $driver"""
    )
    carpool_query = carpool_query_template.substitute(
      id=id,
      max_seats=max_seats,
      driver=0
    )

    # query = "INSERT INTO employee(Employee_ID, First_Name, Last_Name, Address, City, Cannot_Drive, Password, " \
    #         "Admin, Driver_ID, Passenger_Rides, Driver_Rides, Rank) " \
    #         "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # args = (id, fname, lname, address, city, 0, password, 0, 8, 0, 0, 0)
    # print("args: ", args)
    args = (id, fname, lname, address, city, 0, password, 0, 8, 0, 0, 0)
    print("args: ", args)
    mycursor = mydb.cursor()
    mycursor.execute(employee_query)
    mydb.commit()

def update_to_driver(id):
  mydb = mysql.connector.connect(
      host="localhost",
      user="vanessa",
      password="vanessa",
      database='car_pool_planner'
    )

  query_template = Template(
            """UPDATE carpool_groups SET Group_Driver = 1 WHERE fk_Employee_ID = ($id)"""
    )
  query = query_template.substitute(
      id=id
    )
  # print(query)
  mycursor = mydb.cursor()
  mycursor.execute(query)
  mydb.commit()

def update_to_passenger(id):
  mydb = mysql.connector.connect(
      host="localhost",
      user="vanessa",
      password="vanessa",
      database='car_pool_planner'
    )

  query_template = Template(
            """UPDATE carpool_groups SET Group_Driver = 0 WHERE fk_Employee_ID = ($id)"""
    )
  query = query_template.substitute(
      id=id
    )
  # print(query)
  mycursor = mydb.cursor()
  mycursor.execute(query)
  mydb.commit()

def update_group_id(id, group_id):
  mydb = mysql.connector.connect(
      host="localhost",
      user="vanessa",
      password="vanessa",
      database='car_pool_planner'
    )

  query_template = Template(
            """UPDATE carpool_groups SET Group_ID = ($group_id) WHERE fk_Employee_ID = ($id)"""
    )
  query = query_template.substitute(
      id=id,
      group_id = group_id
    )
  print(query)
  mycursor = mydb.cursor()
  mycursor.execute(query)
  mydb.commit()

# insert_employee_db(10, "Max", "Brown", "131 Christie Knoll Point SW", "Calgary", "password10")
# update_to_driver(1)
# update_to_passenger(0)
# update_group_id(0, 0)
data1, data2 = database_to_dic()
print(data1, data2)