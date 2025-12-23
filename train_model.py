import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.read_csv("model/symptoms.csv")

X = data.drop("condition", axis=1)
y = data["condition"]

model = DecisionTreeClassifier()
model.fit(X, y)

pickle.dump(model, open("model/model.pkl", "wb"))
pickle.dump(list(X.columns), open("model/symptom_list.pkl", "wb"))

print("Model trained and symptom list saved!")
