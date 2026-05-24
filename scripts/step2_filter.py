import os
import pandas as pd

# path ke root project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "employees.csv")

# baca data
df = pd.read_csv(file_path)

# filter value
jakarta_only = df[df["kota"] == "Jakarta"]

print("Data Jakarta:")
print(jakarta_only)

# total gaji
total_gaji = df["gaji"].sum()

print("\nTotal Gaji:", total_gaji)