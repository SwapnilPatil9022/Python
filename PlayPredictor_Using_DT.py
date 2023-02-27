""" ----------- Play-Predictor casestudy using DecisionTree algoritham---------------"""
# Requried library's
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn import tree

def PlayPredictor_DecisionTree(data_path):

    # Step 1 : Load Data
    data = pd.read_csv(data_path, index_col=0)

    print("Size of Actual dataset :",len(data))

    # Step 2 : Clean, Prepare and manipulate data
    feature_names = ['Whether','Temperature']

    print("Names of Features", feature_names)

    whether = data.Whether
    Temperature = data.Temperature
    play = data.Play

    # creating labelEncoder
    le = preprocessing.LabelEncoder()

    # Converting string labels into numbers.
    whether_encoded = le.fit_transform(whether)
    print(whether_encoded)

    # Converting string label into numbers
    temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(play)

    print(temp_encoded)

    # Combining wether and temp into single list of tuples
    features = list(zip(whether_encoded,temp_encoded))

    # Step 3 : Train Data
    model = tree.DecisionTreeClassifier()

    # Train the model using the traning sets
    model.fit(features,label)

    first = int(input("Enter the whether number : (1:Rainy, 2:Sunny, 3:Overcast)\n"))
    Secound = int(input("Enter the temprature number : (0:Cool, 1:Hot, 3:Mild)\n"))

    # Step 4 : Test Data
    predicted = model.predict([[first,Secound]]) # 0: Overcast, 2 : Mild
    if predicted == 1:
        print("Now you can play.")
    else:
        print("Don't play.")

def main():
    print("-----------Machine Learning Applicatipon------------")

    print("Play predictor application using DecisionTree classifier algoritham")

    PlayPredictor_DecisionTree("PlayPredictor.csv")

if __name__ == "__main__":
    main()
