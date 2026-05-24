import os
import pandas as pd

# path root project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# input file
input_path = os.path.join(BASE_DIR, "employees.csv")

# output file
output_path = os.path.join(BASE_DIR, "clean_employees.csv")

# load data
df = pd.read_csv(input_path)

# detect duplicate
duplicates = df[df.duplicated()]

print("Duplicate Data:")
print(duplicates)

# clean data
clean_df = df.drop_duplicates()

print("\nClean Data:")
print(clean_df)

# export hasil
clean_df.to_csv(output_path, index=False)

print("\nClean file exported!")