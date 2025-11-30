import pandas as pd
import math

# Load your excel file
df = pd.read_excel("Age Table.xlsx")
df['Age'] = df['Age'].str.strip()

# Only 3 groups: Young, Middle, Old
print(df['Age'].unique())

# Frequency table
freq = pd.crosstab(df['Age'], df['Class'])
print("\nFrequency Table:\n", freq)


# Entropy function
def entropy(col):
    counts = col.value_counts()
    ent = 0
    for c in counts:
        p = c / len(col)
        ent += -p * math.log2(p)
    return ent


# Total entropy of Class
total_entropy = entropy(df['Class'])
print("\nTotal Entropy(Class):", total_entropy)

# Information Gain for AGE
weighted_entropy = 0
total = len(df)

for age_value in ["Young", "Middle", "Old"]:
    subset = df[df['Age'] == age_value]
    ent = entropy(subset['Class'])
    w = len(subset) / total
    weighted_entropy += w * ent

    print(f"Entropy(Class | Age={age_value}) = {ent}")

IG = total_entropy - weighted_entropy
print("\nInformation Gain (Age) =", IG)
