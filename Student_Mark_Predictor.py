# import libararies
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import tree

def Read_File(FileName):
	# Load dataset
	if(os.path.exists(FileName)):
		path = open(FileName,"r")
		df = pd.read_csv(path)
		df.shape
		print(df)

		# Discover and visualize the data
		df.info()
		df.describe()

		plt.scatter(x = df.study_hours, y = df.student_marks)
		plt.xlabel("Student study Hours")
		plt.ylabel("Student Mark")
		plt.title("Scatter plot of Student study Hours VS Student Marks")
		

		# Prepare the data if machine learning algorithams
		# Data Clenning
		df.isnull().sum()
		print("-------------")
		df.mean()
		print("-------------")

		# split datset
		X = df.drop("student_marks", axis = "columns")
		y = df.drop("study_hours", axis = "columns")
		print("shape of X = ",X.shape)
		print("shape of y = ",y.shape)
		print("-----------------------------------")

		X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 51)
		print("shape of X_train = ",X_train.shape)
		print("shape of y_train = ",y_train.shape)
		print("shape of X_test = ",X_test.shape)
		print("shape of y_test = ",y_test.shape)

		obj = tree.DecisionTreeClassifier()

		obj = obj.fit(X_train,y_train)

		ret = (obj.predict([[4]]))
		print(ret)

		# Leaniear regration
		# y = m * x + c
		print("==================================")
		lr = LinearRegression()
		lr.fit(X_train,y_train)
		print(lr.fit)
		lr.coef_
		lr.intercept_
		lr.predict([[4]])


	else:
		print("File is not existing")
		return 

def main():
	print("Enter the file name to read")
	Name = input()

	Read_File(Name)

if __name__ == "__main__":
	main()