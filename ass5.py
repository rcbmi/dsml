import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv("Lipstick.csv")

print(data.head())

## Encode the categorical variables

label_encoders = {}

for column in data.columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

## Split features(X) and target(y)

X = data[["Age", "Income", "Gender", "Ms"]]
y = data["Buys"]


## Train the decision tree

clf = DecisionTreeClassifier(criterion="entropy", random_state=42)
clf.fit(X,y)


## Test Data Prediction

test_data = pd.DataFrame([["<21","Low","Female","Married"]],columns=["Age","Income","Gender","Ms"])

for column in test_data.columns:
    test_data[column] = label_encoders[column].transform(test_data[column])

prediction = clf.predict(test_data)
predicted_label = label_encoders["Buys"].inverse_transform(prediction)


# Display Results

print(f"Test data prediction: {predicted_label[0]}")

tree_rules = export_text(clf, feature_names=["Age","Income","Gender","Ms"])
print("\nDecision Tree Rules:")
print(tree_rules)




