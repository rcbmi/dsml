import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Titanic.csv")

print(df.head())

plt.figure(figsize=(8,6))
sns.histplot(df['Fare'],kde=True,bins=30,color="blue")
plt.title("Distribution of ticket Prices (Fare) for titanic passengers:")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.show()

