import sqlite3
import pandas as pd

# connect database
conn = sqlite3.connect("company.db")

# read csv
df = pd.read_csv("clean_employees.csv")

# transform data
df["kategori_gaji"] = df["gaji"].apply(
    lambda x: "High" if x >= 7000 else "Low"
)

print(df)

# insert to database
df.to_sql("employees", conn, if_exists="replace", index=False)

# query database
query = """
SELECT *
FROM employees
"""

result = pd.read_sql(query, conn)

print(result)

# close connection
conn.close()