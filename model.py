import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Make sure the CSV 'Copy of sonar data.csv' is in the same folder
sonar_data = pd.read_csv("C:/Users/Shanthini/OneDrive/Desktop/Git tutorial/Copy of sonar data.csv" )


X = sonar_data.drop(columns='R', axis=1)
y = sonar_data['R']


x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)


model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)


# evaluate (optional)
y_pred = model.predict(x_test)
print('Test accuracy:', accuracy_score(y_test, y_pred))


# save with pickle
with open('model.pkl', 'wb') as f:
 pickle.dump(model, f)


print('Model saved to model.pkl')