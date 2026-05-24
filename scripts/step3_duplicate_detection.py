import pandas as pd

df = pd.read_csv("employees.csv")

duplicates = df[df.duplicated()]

print("Duplicate Data:")
print(duplicates)

clean_df = df.drop_duplicates()

print("Clean Data:")
print(clean_df)