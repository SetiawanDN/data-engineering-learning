import sqlite3
import pandas as pd

# connect database
conn = sqlite3.connect("company.db")

# read csv
df = pd.read_csv("clean_employees.csv")

# insert ke database
df.to_sql("employees", conn, if_exists="replace", index=False)

print("Data inserted into database!")

# query database
query = "SELECT * FROM employees"

result = pd.read_sql(query, conn)

print(result)

# close connection
conn.close()