import matplotlib.pyplot as plt

import pandas as pd
num_df=pd.read_csv("House Data.csv")
print(num_df.head())


print(num_df.describe())


# standard deviation
print(num_df.std(numeric_only=True))


# variance
print(num_df.var(numeric_only=True))


# 25th percentile
df_valid=num_df.select_dtypes(include=['int64','float64'])
print(df_valid.quantile(0.25,numeric_only=True))


# 50th percentile

print(df_valid.quantile(0.50,numeric_only=True))


# 75th percentile

print(df_valid.quantile(0.75,numeric_only=True))


num_df = num_df.drop(columns=['Unnamed: 0'])

for column in num_df.columns:
    plt.figure(figsize=(10,6))
    plt.hist(num_df[column].dropna())
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.xticks(rotation=90)
    plt.show()






#
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Load dataset
# df = pd.read_csv("House Data.csv")
#
# # ==============================
# # 1. Data Preprocessing
# # ==============================
#
# # Handle missing values
# for col in df.columns:
#     if df[col].isnull().sum() > 0:
#         if df[col].dtype in ["int64", "float64"]:
#             df[col] = df[col].fillna(df[col].mean())
#         else:
#             df[col] = df[col].fillna(df[col].mode()[0])
#
# # Remove duplicates
# df = df.drop_duplicates()
#
# # Convert price to numeric if exists
# if "price" in df.columns:
#     df["price"] = df["price"].astype(str)
#     df["price"] = df["price"].str.replace(r"[^0-9]", "", regex=True)
#     df["price"] = pd.to_numeric(df["price"], errors="coerce")
#     df["price"] = df["price"].fillna(df["price"].mean())
#
# # ==============================
# # 2. Numeric Features Only
# # ==============================
# numeric_df = df.select_dtypes(include=["int64", "float64"])
#
# print("\nNumeric Features:")
# print(numeric_df.columns)
#
# # ==============================
# # 3. Standard Deviation
# # ==============================
# std_dev = numeric_df.std()
# print("\nStandard Deviation:\n", std_dev)
#
# # ==============================
# # 4. Variance
# # ==============================
# variance = numeric_df.var()
# print("\nVariance:\n", variance)
#
# # ==============================
# # 5. Percentiles
# # ==============================
# percentiles = numeric_df.quantile([0.25, 0.5, 0.75])
# print("\nPercentiles (25%, 50%, 75%):\n", percentiles)
#
# # ==============================
# # 6. Histogram Plots
# # ==============================
# for col in numeric_df.columns:
#     plt.figure()
#     plt.hist(numeric_df[col], bins=20)
#     plt.title(f"Histogram of {col}")
#     plt.xlabel(col)
#     plt.ylabel("Frequency")
#     plt.grid(True)
#     plt.show()
