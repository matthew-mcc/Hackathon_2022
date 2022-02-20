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


print(employee_df)

employee_df.to_csv("employees.csv")
carpool_groups_df.to_csv("carpool_groups.csv")
driver_df.to_csv("driver.csv")
company_df.to_csv("company.csv")
