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




# import pandas as pd
#
# # Load Titanic dataset
# df = pd.read_csv("Titanic.csv")
#
# # =========================
# # 1. Data Cleaning
# # =========================
#
# # Fill missing values
# df["Age"] = df["Age"].fillna(df["Age"].mean())
# df["Fare"] = df["Fare"].fillna(df["Fare"].median())
# df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
#
# # Cabin has too many missing values → replace with "Unknown"
# df["Cabin"] = df["Cabin"].fillna("Unknown")
#
# # Remove duplicate rows
# df = df.drop_duplicates()
#
# # Clean text columns
# df["Name"] = df["Name"].str.strip()
# df["Ticket"] = df["Ticket"].str.strip()
# df["Cabin"] = df["Cabin"].str.strip()
#
# # Convert categorical text to lowercase
# df["Embarked"] = df["Embarked"].str.lower()
# df["Sex"] = df["Sex"].str.lower()
#
# # =========================
# # 2. Data Transformation
# # =========================
#
# # Convert Sex to numerical
# df["Sex"] = df["Sex"].map({"male": 1, "female": 0})
#
# # Create new column: Survival Status
# df["Survival_Status"] = df["Survived"].apply(lambda x: "Survived" if x == 1 else "Not Survived")
#
# # Create Age Group column
# df["Age_Group"] = pd.cut(
#     df["Age"],
#     bins=[0, 12, 20, 35, 60, 100],
#     labels=["Child", "Teen", "Young Adult", "Adult", "Senior"]
# )
#
# # Normalize Age and Fare
# df["Normalized_Age"] = (df["Age"] - df["Age"].min()) / (df["Age"].max() - df["Age"].min())
# df["Normalized_Fare"] = (df["Fare"] - df["Fare"].min()) / (df["Fare"].max() - df["Fare"].min())
#
# # Rename Fare column
# df.rename(columns={"Fare": "Ticket_Fare"}, inplace=True)
#
# # =========================
# # Final Output
# # =========================
# print("✅ Titanic Data Cleaning & Transformation Completed\n")
# print(df.head())
#
# # Save cleaned dataset
# df.to_csv("Titanic_Cleaned_Transformed.csv", index=False)
