import pandas as pd
df_num=pd.read_csv("Covid Vaccine Statewise.csv")
print(df_num.shape)
print(df_num.info())

print(df_num.head())

print(df_num.describe())

print(df_num.columns)

firstDose=df_num.groupby("State")["First Dose Administered"].sum()
print(firstDose)

secondDose=df_num.groupby("State")["Second Dose Administered"].sum()
print(secondDose)




