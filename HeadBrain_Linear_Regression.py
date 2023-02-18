"""
  * Above data set contains information about Head and Brain size depends on gender and age.
	
	Consider below characteristics of Machine Learning Application.

	Classifier : 	Linear Regression
	Dataset :  		HeadBrain Dataset
	Features :		Gender, Age, Head size, Brain weight
	Labels : 		-
	Training Dataset : 237
"""
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def HeadBrainPredictor():
	# Load data
	data = pd.read_csv("HeadBrain.csv")

	print("Size of data set",data.shape)

	X = data['Head Size(cm^3)'].values
	Y = data['Brain Weight(grams)'].values

	X = X.reshape((-1,1))

	n = len(X)

	reg = LinearRegression()

	reg = reg.fit(X,Y)

	y_pred = reg.predict(X)

	r2 = reg.score(X,Y)
	print("------------------")
	print(r2)

def main():
	print("-----LinearRegression of HeadBrain Casestudy by Swapnil Patil-----")

	print("Supervised Machine Learning")

	print("Linear Regression on Head and Brain size data set")

	HeadBrainPredictor()

if __name__ == "__main__":
	main()

