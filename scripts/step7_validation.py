import sqlite3
import pandas as pd

conn = sqlite3.connect("company.db")

df = pd.read_csv("employees.csv")

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

print("Cleaned Data:")
print(df)

# load to database
df.to_sql("employees", conn, if_exists="replace", index=False)

print("Data loaded successfully!")

conn.close()