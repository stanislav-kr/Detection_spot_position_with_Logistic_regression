"""This is the main file and contains functions for training and testing the model"""

import pandas as pd
import numpy as np
from dataset import load_data
from sklearn.metrics import recall_score, precision_score, f1_score, classification_report

x_train, x_test, y_train, y_test = load_data()


class LogisticRegression:
    """Class accepts two parameters: learning_rate and epochs, which are model hyperparameters."""

    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs

    """Function to transform numbers into values in the range from 0 to 1"""

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    """Function to train the model"""

    def train(self, x_train, y_train):
        x_train = np.insert(x_train, 0, 1, axis=1)
        self.weights = np.zeros(x_train.shape[1])

        # Calculating class weights
        total = len(y_train)
        count_0 = np.sum(y_train == 0)
        count_1 = np.sum(y_train == 1)
        weight_0 = total / (2.5 * count_0)
        weight_1 = total / (2 * count_1)

        for _ in range(self.epochs):
            z = np.dot(x_train, self.weights)
            predictions = self.sigmoid(z)

            # Weights for each label
            sample_weights = np.where(y_train == 1, weight_1, weight_0)

            # Gradient
            gradient = np.dot(x_train.T, sample_weights * (predictions - y_train)) / total
            self.weights -= self.learning_rate * gradient

    """Function returning probability values using the sigmoid function"""

    def predict_prob(self, x_test):
        x_test = np.insert(x_test, 0, 1, axis=1)
        return self.sigmoid(np.dot(x_test, self.weights))

    """Function checking if the value exceeds a specified threshold"""

    def predict(self, x_test):
        return self.predict_prob(x_test) >= 0.6


model = LogisticRegression(learning_rate=0.1, epochs=1000)
model.train(x_train, y_train)

"""Checks if the file is run as main and if so, executes the code below"""
if __name__ == "__main__":
    y_pred = model.predict(x_test)

    accuracy = np.mean(y_pred == y_test)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"Accuracy:  {accuracy:.2f}")
    print(f"Recall:    {recall:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"F1 Score:  {f1:.2f}")

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, digits=3))
