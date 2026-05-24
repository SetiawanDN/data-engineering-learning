import os
import sqlite3
import pandas as pd

# root project path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# file paths
csv_path = os.path.join(BASE_DIR, "clean_employees.csv")
db_path = os.path.join(BASE_DIR, "company.db")

# connect database
conn = sqlite3.connect(db_path)

# read csv
df = pd.read_csv(csv_path)

# transform data
df["kategori_gaji"] = df["gaji"].apply(
    lambda x: "High" if x >= 7000 else "Low"
)

print("Transformed Data:")
print(df)

# insert to database
df.to_sql("employees", conn, if_exists="replace", index=False)

# query database
query = """
SELECT *
FROM employees
"""

result = pd.read_sql(query, conn)

print("\nDatabase Result:")
print(result)

# close connection
conn.close()