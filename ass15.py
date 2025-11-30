import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("Titanic.csv")

print(df.head())


print(df.columns)

print(df.info())


# 1.Survival Count
plt.figure()
sns.countplot(x='Survived',data=df)
plt.title("Survival Count (0=Not Survived,1=Survived)")
plt.show()
# more people died than survived


# 2.Survival vs Gended
plt.figure()
sns.countplot(x='Survived',hue="Sex",data=df)
plt.title("Survival Based on Gender")
plt.show()
# large number of males did not survived buto large number of females survived this suggests that female were given more priority


print(df['Survived'].sum())

# Surviavl based on passenger class

plt.figure()
sns.countplot(x='Pclass',hue='Survived',data=df)
plt.title("Survival Based on pasenger class")
plt.show()


# Age distribution
plt.figure(figsize=(8,6))
sns.histplot(data=df,x="Age",hue="Survived",multiple='stack',kde=True)
plt.title("Age distribution of passengers")
plt.show()


## Survival Rate based on Embarked Port

plt.figure(figsize=(8, 6))
sns.countplot(x='Embarked', hue='Survived', data=df)
plt.title('Survival Rate Based on Embarked Port')
plt.show()


# Fare distribution
plt.figure()
sns.histplot(df['Fare'],bins=30,kde=True)
plt.title("Fare Distribution of passengers")
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()


