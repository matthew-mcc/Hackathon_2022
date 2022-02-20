from re import TEMPLATE
from tokenize import group
import mysql.connector
import pandas as pd
from string import Template

def database_to_dict():
  mydb = mysql.connector.connect(
    host="localhost",
    user="vanessa",
    password="vanessa",
    database='car_pool_planner'
  )

  employee_df = pd.read_sql("SELECT * FROM employee", con=mydb)
  carpool_groups_df = pd.read_sql("SELECT * FROM carpool_groups", con=mydb)
  driver_df = pd.read_sql("SELECT * FROM driver", con=mydb)
  company_df = pd.read_sql("SELECT * FROM company", con=mydb)

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
          VALUES($id, \"$fname\", \"$lname\", \"$address\", \"$city\", \"$password\", $admin, $rides, $drives)"""
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
    drives=0
    )

  # Driver Query
  driver_query_template = Template(
          """INSERT INTO driver
          VALUES($id, $max_seats, $max_distance_km)"""
  )
  driver_query = driver_query_template.substitute(
    id=id,
    max_seats=max_seats,
    max_distance_km=10
  )

  # Carpool Query
  carpool_query_template = Template(
            """INSERT INTO carpool_groups
            VALUES($group_id, $id, $driver)"""
  )
  carpool_query = carpool_query_template.substitute(
    group_id=0,
    id=id,
    driver=0
  )

  mycursor = mydb.cursor()
  mycursor.execute(employee_query)
  mycursor.execute(driver_query)
  mycursor.execute(carpool_query)
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
  mycursor = mydb.cursor()
  mycursor.execute(query)
  mydb.commit()


def change_drivers():
  mydb = mysql.connector.connect(
  host="localhost",
  user="vanessa",
  password="vanessa",
  database='car_pool_planner'
  )
  carpool_groups_df = pd.read_sql("SELECT * FROM carpool_groups", con=mydb, index_col="fk_Employee_ID")
  for label, item in carpool_groups_df.iterrows():
    if item["Group_Driver"] == 1:
      update_to_passenger(label)
      if (label < carpool_groups_df["Group_Driver"].size-1):
        update_to_driver(label + 1)
      else:
        update_to_driver(0)


# Returns a list of first name, last name, and address of employee in group with group_id number
def group_to_list(group_id):
  mydb = mysql.connector.connect(
      host="localhost",
      user="vanessa",
      password="vanessa",
      database='car_pool_planner')
  query_template = Template(
    """SELECT First_Name, Last_Name, Address, Group_Driver FROM employee, carpool_groups WHERE carpool_groups.Group_id = ($group_id) AND carpool_groups.fk_Employee_ID = employee.Employee_ID"""
    )
  query = query_template.substitute(
      group_id = group_id
    )
  mycursor = mydb.cursor()
  mycursor.execute(query)

  myresult = mycursor.fetchall()
  
  return myresult

def remove_user(id: int):
  mydb = mysql.connector.connect(
      host="localhost",
      user="vanessa",
      password="vanessa",
      database='car_pool_planner')
  
  employee_query = f"DELETE FROM employee WHERE Employee_ID={id}"
  driver_query = f"DELETE FROM driver WHERE fk_Employee_ID={id}"
  carpool_groups = f"DELETE FROM carpool_groups WHERE fk_Employee_ID={id}"

  mycursor = mydb.cursor()

  mycursor.execute(employee_query)
  mycursor.execute(driver_query)
  mycursor.execute(carpool_groups)

  mydb.commit()

result = group_to_list(0)
for x in result:
  print(x)

# Returns a list with first name, last name, and address as list inputs
def get_fname_lname_address(id: int):
  mydb = mysql.connector.connect(
    host="localhost",
    user="vanessa",
    password="vanessa",
    database="car_pool_planner"
  )
  mycursor = mydb.cursor()

  query = f"SELECT First_Name, Last_Name, Address FROM employee WHERE Employee_ID={id}"

  mycursor(query)

  myresult = mycursor.fetchall()

  fname = myresult[0]
  lname = myresult[1]
  address = myresult[2]

  return fname, lname, address