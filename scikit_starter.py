import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def create_dataset(data, n_predictions):
    X, y = [], []
    for i in range(len(data) - n_predictions):
        X.append(data[i:i + n_predictions])
        y.append(data[i + n_predictions])
    return np.array(X), np.array(y)

data = [float(x) for x in input('CatDog wants to buy treats.\nCatDog needs to know how many treats they should eat for the next few days.\nEnter a series of numbers that are separated by space (e.g., "1 2 3 4 5"):\n').split()]

n_predictions = int(input('CatDog wants a machine to predict how many treats they will eat after that.\nEnter number of predictions: '))

X, y = create_dataset(data, n_predictions)

X_df = pd.DataFrame(X)
y_df = pd.Series(y)

model = LinearRegression()
model.fit(X_df, y_df)

last_sequence = np.array(data[-n_predictions:]).reshape(1, -1)
predicted = []

for _ in range(n_predictions):
    next_value = model.predict(last_sequence)[0]
    predicted.append(next_value)
    last_sequence = np.append(last_sequence[:, 1:], next_value).reshape(1, -1)

print(f"\nThe next {n_predictions} predicted number of treats CatDog will eat are: {str(predicted).strip('[]')}")
