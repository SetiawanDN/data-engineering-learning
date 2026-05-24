import os
import pandas as pd

# ambil path root project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "employees.csv")

# load data
df = pd.read_csv(file_path)

# detect duplicate
duplicates = df[df.duplicated()]

print("Duplicate Data:")
print(duplicates)

# clean data
clean_df = df.drop_duplicates()

print("\nClean Data:")
print(clean_df)