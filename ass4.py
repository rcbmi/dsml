import pandas as pd
import math

data=pd.read_csv("Lipstick.csv")

print(data.head())

# How do I delete the Id column of the dataset
data.drop('Id', axis=1, inplace=True)


# function to calculate entropy
def calculate_entropy(data, target_column):
    values = data[target_column].value_counts()
    entropy = 0
    for count in values:
        probability = count/len(data)
        entropy -= probability * math.log2(probability)
    return entropy


# function to calculate information gain
def calculate_information_gain(data, attribute, target_col):
    total_entropy = calculate_entropy(data, target_col)

    # calculate weighted entropy for the attribute
    values = data[attribute].value_counts(normalize=True)
    weighted_entropy = sum(
        values[value] * calculate_entropy(data[data[attribute] == value], target_col)
        for value in values.index
    )

    # information gain
    info_gain = total_entropy - weighted_entropy
    return info_gain


# step-by-step decision tree creation
target_column = "Buys"
attributes = [col for col in data.columns if col != target_column]

# calculate information gain for each attributes
info_gains = {}
for attribute in attributes:
    info_gains[attribute] = calculate_information_gain(data, attribute, target_column)


# Find the root node
root_node = max(info_gains, key=info_gains.get)


# display the results
print("Information Gain for each attribute:")
for attr, gain in info_gains.items():
    print(f"{attr} : {gain}")

print(f"\nRoot Node of the Decision Tree: {root_node}")

