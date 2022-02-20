import mysql.connector
import pandas as pd
from mysql.connector import Error

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


print(employee_df)

employee_df.to_csv("employees.csv")
carpool_groups_df.to_csv("carpool_groups.csv")
driver_df.to_csv("driver.csv")
company_df.to_csv("company.csv")


def insert_employee_db(id, fname, lname, address, city, password):
    query = "INSERT INTO employee(Employee_ID, First_Name, Last_Name, Address, City, Cannot_Drive, Password, " \
            "Admin, Driver_ID, Passenger_Rides, Driver_Rides, Rank) " \
            "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    args = (id, fname, lname, address, city, 0, password, 0, 8, 0, 0, 0)
    print("args: ", args)
    mycursor = mydb.cursor()
    mycursor.execute(query, args)
    mydb.commit()
    # try:
    #     # db_config = read_db_config()
    #     # conn = MySQLConnection(**db_config)

    #     mycursor = mydb.cursor()
    #     mycursor.execute(query, args)

    #     if mycursor.lastrowid:
    #         print('last insert id', mycursor.lastrowid)
    #     else:
    #         print('last insert id not found')

    #     mydb.commit()
    # except Error as error:
    #     print(error)

    # finally:
    #     mycursor.close()
    #     mydb.close()

insert_employee_db(10, "Max", "Brown", "131 Christie Knoll Point SW", "Calgary", "password10")
