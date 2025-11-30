import pandas as pd

# Load your dataset
df = pd.read_csv("House Data.csv")   # <-- change filename if needed

# Automatically identify categorical & quantitative variables
categorical_vars = df.select_dtypes(include=['object', 'category']).columns
quantitative_vars = df.select_dtypes(include=['int64', 'float64']).columns

print("Categorical Variables:", list(categorical_vars))
print("Quantitative Variables:", list(quantitative_vars))

# Function to compute summary statistics grouped by categorical variable
def grouped_summary(df, cat_var, num_var):
    return df.groupby(cat_var)[num_var].agg(
        Mean='mean',
        Median='median',
        Min='min',
        Max='max',
        Std_Dev='std'
    )

# Generate summary statistics for each (categorical, quantitative) pair
for cat in categorical_vars:
    for num in quantitative_vars:
        print(f"\n===== Summary of '{num}' grouped by '{cat}' =====")
        print(grouped_summary(df, cat, num))

# import pandas as pd
#
# df = pd.read_csv("House Data.csv")
#
# # Clean price column
# df['price'] = df['price'].astype(str)
# df['price'] = df['price'].str.replace(r'[^0-9]', '', regex=True)
#
# df['numeric_price'] = pd.to_numeric(df['price'], errors='coerce')
#
# # Remove rows where price could not be converted
# df = df.dropna(subset=['numeric_price'])
#
# # Define categorical and quantitative variables
# categorical = 'district'       # Example categorical
# quantitative = 'numeric_price' # Example quantitative
#
# # Group and calculate statistics
# values = df.groupby(categorical)[quantitative].agg([
#     'count',
#     'mean',
#     'median',
#     'min',
#     'max',
#     'std'
# ])
#
# print(values)