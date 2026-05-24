import os
import sqlite3
import pandas as pd

# root project path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# file paths
csv_path = os.path.join(BASE_DIR, "employees.csv")
db_path = os.path.join(BASE_DIR, "company.db")

# connect database
conn = sqlite3.connect(db_path)

# read data (FIX UTAMA)
df = pd.read_csv(csv_path)

# check missing data
missing_data = df[df.isnull().any(axis=1)]

print("Missing Data:")
print(missing_data)

# fill missing kota
df["kota"] = df["kota"].fillna("Unknown")

# transform salary category
df["kategori_gaji"] = df["gaji"].apply(
    lambda x: "High" if x >= 7000 else "Low"
)

print("\nCleaned Data:")
print(df)

# load to database
df.to_sql("employees", conn, if_exists="replace", index=False)

print("\nData loaded successfully!")

conn.close()