from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from scipy.spatial import distance

def euc(a,b):
	return distance.euclidean(a,b)

class MarvellousKNeighborsClassifier:

	def fit(self,trainingdata, trainingtarget):
		self.TreaningData = trainingdata
		self.TraninngTarget = trainingtarget

	def closest(self, row):
		minimumdistance = euc(row, self.TreaningData[0])
		minimumindex = 0

		for i in range(1,len(self.TreaningData)):
			Distance = euc(row, self.TreaningData[i])
			if Distance < minimumdistance:
				minimumdistance = Distance
				minimumindex = i

		return self.TraninngTarget[minimumindex]

	def predict(self, TestData):
		Predictions = []
		for value in TestData:
			result = self.closest(value)
			Predictions.append(result)

		return Predictions

def MarvellousML():
	Dataset = load_iris()		# 1 Load the data

	Data = Dataset.data
	Target = Dataset.target

	Data_train, Data_test, Target_train, Target_test = train_test_split(Data, Target, test_size = 0.5)

	Classifire = MarvellousKNeighborsClassifier()

	Classifire.fit(Data_train, Target_train)

	Predictions = Classifire.predict(Data_test)

	Accuracy = accuracy_score(Target_test, Predictions)

	return Accuracy

def main():
	Ret = MarvellousML()

	print("Accuracy of Iris dataset with KNN is :",Ret * 100)

if __name__ == "__main__":
	main()