# Diabetes Predictor application using Decision Tree algoritham.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

print("----- Diabetes predictor using Decision Tree-----") 

diabetes = pd.read_csv("diabetes.csv")

print("Columns of Dataset")
print("diabetes.columns")

print("First 5 records of dataset")
print(diabetes.head())

print("Dimension of daibetes data : {}".format(diabetes.shape))

X_train, X_test, Y_train, Y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify = diabetes['Outcome'], random_state = 66)

tree = DecisionTreeClassifier(random_state = 0)
tree.fit(X_train, Y_train)

print("Accuracy on training set : {:.3f}".format(tree.score(X_train, Y_train)))

print("Accuracy on test set : {:.3f}".format(tree.score(X_test, Y_test)))

tree = DecisionTreeClassifier(max_depth = 3, random_state = 0)
tree.fit(X_train, Y_train)

print("Accuracy on training set : {:.3f}".format(tree.score(X_train, Y_train)))
print("Accuracy on test set : {:.3f}".format(tree.score(X_test, Y_test)))

print("Feature importances:\n{}".format(tree.feature_importances_))

def plot_feature_importances_diabetes(model):
	plt.figure(figsize=(8,6))
	n_features = 8
	plt.barh(range(n_features), model.feature_importances_, align = 'center')
	diabetes_features = [X for i,X in enumerate(diabetes.columns) if i!=8]
	plt.yticks(np.arange(n_features), diabetes_features)
	plt.xlabel("Feature importances")
	plt.ylabel("Feature")
	plt.ylim(-1, n_features)
	plt.show()

plot_feature_importances_diabetes(tree)
