import pandas as pd

df = pd.read_csv("employees.csv")

jakarta_only = df[df["kota"] == "Jakarta"]

print(jakarta_only)

total_gaji = df["gaji"].sum()

print("Total Gaji:", total_gaji)