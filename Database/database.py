import mysql.connector
import pandas as pd;

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

print(employee_df)
