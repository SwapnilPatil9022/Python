# Diabetes Predictor application using Decision Tree algoritham.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from warnings import simplefilter

print("----- Diabetes predictor using KNN-----") 

diabetes = pd.read_csv("diabetes.csv")

print("Columns of Dataset")
print("diabetes.columns")

print("First 5 records of dataset")
print(diabetes.head())

print("Dimension of daibetes data : {}".format(diabetes.shape))

X_train, X_test, Y_train, Y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify = diabetes['Outcome'], random_state = 66)

training_accuracy = []
test_accuracy = []

# try n_neighbors from 1 to 10
neighbors_setting = range(1,11)

for n_neighbors in neighbors_setting:
	# Build the model
	knn = KNeighborsClassifier(n_neighbors=n_neighbors)
	knn.fit(X_train,Y_train)
	# record test set accuracy
	test_accuracy.append(knn.score(X_test,Y_test))

plt.plot(neighbors_setting,training_accuracy, label = "training accuracy")
plt.plot(neighbors_setting, test_accuracy,label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()x
plt.savefig("knn_compare_model")
plt.show()

knn.fit(X_train,Y_train)

print("Accuracy of kNN on traning set : {:.2f}".format(knn.score(X_train, Y_train)))
print("Accuracy of kNN on test set : {:.2f}".format(knn.score(X_test, Y_test)))
