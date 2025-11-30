import pandas as pd

df_csv=pd.read_csv("Titanic.csv")
print(df_csv.head(),'\n')
# df_exl=pd.read_excel("tested.xls")

df=df_csv

# select a single column
print("Name Column")
print(df["Name"].head())

print("Name and Sex column")
print(df[["Name","Sex"]].head())

# to access row by its index
print(df.loc[0])

print(df.iloc[1:5])
# will print data for row 1 to row 4


print(df.loc[0:5])
# print data for all rows qith index 0 to 5



print("Passengers with age>50")
print(df[df["Age"]>50].head())

# 4.Sorting the data
# sort by age in ascending order
df_sorted_age=df.sort_values(by="Age")

print(df_sorted_age[["Name","Sex","Ticket","Fare","Age"]].head())



df_sorted_multi=df.sort_values(by=["Pclass","Fare"],ascending=[True,False])
print("data sorted by Pclass (asc) and Fare (desc):")
print(df_sorted_multi[["Name","Sex","Pclass","Fare","Age"]].head())



# Describing attributes of data
print("Summary statistics of numerical data")
print(df.describe())




print("Summmary for all columns including object type")
print(df.describe(include="all"),"\n")




# print datatypes
print(df.dtypes,"\n")



# for more info including datatypes
print(df.info())

print("\nSelecting the first 3 rows and specific columns (Name, Age):")
print(df.loc[:2, ['Name', 'Age']])  # Adjust columns based on your dataset structure



