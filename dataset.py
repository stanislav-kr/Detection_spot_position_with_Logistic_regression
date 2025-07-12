"""This file contains functions for data normalization and splitting"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

"""Function to normalize data to the range [0,1]"""


def normalization(data, min_elem, max_elem):
    data['footForce'] = data['footForce'].apply(lambda x: np.array(x))
    data['footForce'] = data['footForce'].apply(lambda x: (x - min_elem) / (max_elem - min_elem))
    return data


"""Function creating a new column with labels"""


def labeling(data):
    data['onstairs'] = data['imu'].apply(
        lambda imu_dict: 1 if (imu_dict['rpy'][1] > 0.2094396 or imu_dict['rpy'][1] < -0.2094396) else 0)
    return data


"""Function returning the maximum and minimum values in the dataset"""


def get_min_max(data):
    all_values = np.concatenate(data.to_list())
    return np.min(all_values), np.max(all_values)


"""Main function for data processing"""


def load_data():
    data = pd.read_json('bla bla bla')
    data = labeling(data)
    dataMove = data[['footForce', 'onstairs']]
    dataMove = dataMove.copy()
    x = dataMove[['footForce']]    # feature selection
    y = dataMove['onstairs']  # label selection
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,
                                                        random_state=42)   # data split: 80% train, 20% test
    min_elem, max_elem = get_min_max(x_train['footForce'])

    x_train = normalization(x_train, min_elem, max_elem).values    # feature normalization
    x_test = normalization(x_test, min_elem, max_elem).values # feature normalization

    x_train = np.array([x[0] for x in x_train])  # unpacking numpy arrays
    x_test = np.array([x[0] for x in x_test])
    return x_train, x_test, y_train, y_test
