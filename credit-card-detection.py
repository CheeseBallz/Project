import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# load dataset
data = pd.read_csv("small_creditcard.csv") # add your own file path here

# features and target
X = data.drop("Class", axis=1)
y = data["Class"]

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# train model with class imbalance handling
model = LogisticRegression(max_iter=1000, class_weight="balanced")
model.fit(X_train, y_train)

# predictions
y_pred = model.predict(X_test)

# evaluation
print("Fraud Detection Results\n")

print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))