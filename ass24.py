import pandas as pd

# 1. Load a suitable dataset (Titanic test dataset here)
df = pd.read_csv("Titanic.csv")   # use your filename, e.g. "Titanic_test.csv"

# 2. Count unique values of each column
print("=== Unique value counts for each column ===")
print(df.nunique())
print("\n")

# 3. Format (data type) of each column
print("=== Data types of each column (before conversion) ===")
print(df.dtypes)
print("\n")

# 4. Example of converting variable data types
#    Convert PassengerId from int64 to int32
df["PassengerId"] = df["PassengerId"].astype("int32")

#    Convert Age and Fare from float64 to float32 (if they exist)
if "Age" in df.columns:
    df["Age"] = df["Age"].astype("float32")
if "Fare" in df.columns:
    df["Fare"] = df["Fare"].astype("float32")

print("=== Data types of each column (after conversion) ===")
print(df.dtypes)
print("\n")

# 5. Identify missing values
print("=== Missing values in each column ===")
print(df.isna().sum())
print("\n")

# 6. Fill missing values
# For numeric columns: fill with mean
numeric_cols = df.select_dtypes(include=["int16","int32","int64","float16","float32","float64"]).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# For categorical (object) columns: fill with mode (most frequent value)
categorical_cols = df.select_dtypes(include=["object"]).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("=== Missing values after filling ===")
print(df.isna().sum())
