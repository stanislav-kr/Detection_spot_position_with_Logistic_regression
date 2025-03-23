"""This file was create for separiting, normalizing and cleaning data"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

"""Self labeling data <-_->"""


def self_labeling(data):
    data['onstairs'] = data['footForce'].apply(
        lambda x: True if x[2] + x[3] - (x[0] + x[1]) > 100 or x[0] + x[1] - (x[2] + x[3]) > 100 else False)
    return data


def normalization(data):
    max_elem = max(max(sublist) for sublist in data['footForce'])
    min_elem = min(min(sublist) for sublist in data['footForce'])
    data['footForce'] = data['footForce'].apply(lambda x: np.array(x))
    data['footForce'] = data['footForce'].apply(lambda x: (x - min_elem) / (max_elem - min_elem))
    return data


data = pd.read_json('data.json')
dataMove = data[['footPosition2Body', 'footForce']]
dataMove = dataMove.copy()
print(dataMove)
dataMove = self_labeling(dataMove)
print('\n', dataMove)
x = dataMove[['footPosition2Body', 'footForce']]
y = dataMove[['onstairs']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("================================================")
print('\n', x_train)
print("================================================")
x_train = normalization(x_train)
x_test = normalization(x_test)
print('\n', x_train['footForce'])
print("================================================")
print('\n', x_test['footForce'])
