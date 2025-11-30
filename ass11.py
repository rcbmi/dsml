import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("IRIS.csv")
print(df.head())

if 'Id' in df.columns:
    df = df.drop("Id", axis=1)

num_df = df.select_dtypes(include=['int64', 'float64'])

print("Features in dataset", list(df.columns))

print("\nNumeric Features", list(num_df.columns))

print(df.dtypes)

for column in num_df.columns:
    plt.figure()
    plt.hist(num_df[column])
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()






