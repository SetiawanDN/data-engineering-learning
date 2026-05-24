import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "employees.csv")

df = pd.read_csv(file_path)

print("Data loaded:")
print(df.head())