import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("IRIS.csv")

print(df.head())

if 'Id' in df.columns:
    df = df.drop("Id", axis=1)

print(df.dtypes)
num_df = df.select_dtypes(include=['int64', 'float64'])

print(num_df.columns)

# Boxplot for each feature

for column in num_df.columns:
    plt.figure()
    plt.boxplot(num_df[column].dropna())
    plt.title(f"Box Plot of {column}")
    plt.ylabel(column)
    plt.show()

print(num_df.columns)


for column in num_df.columns:
    Q1 = num_df[column].quantile(0.25)
    Q3 = num_df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = num_df[(num_df[column] < lower_bound) | (num_df[column] > upper_bound)][column]
    print(f"Feature:{column}")
    print(f"Q1={Q1}")
    print(f"Q3={Q3}")
    print(f"IQR={IQR}")
    print(f"Lower Bound:{lower_bound}")
    print(f"Upper_bound:{upper_bound}")

    if len(outliers) == 0:
        print("no outliers found")
    else:
        print("Outliers are")
        print(outliers.values)



