
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):

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
    model = KNeighborsClassifier(n_neighbors = 3)

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

    print("Play predictor application using K Nearest Knighbor algoritham")

    MarvellousPlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()















"""

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):

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
    model = KNeighborsClassifier(n_neighbors = 3)

    # Train the model using the traning sets
    model.fit(features,label)

    # Step 4 : Test Data
    predicted = model.predict([[0,2]]) # 0: Overcast, 2 : Mild
    print(predicted)

def main():
    print("-----------Machine Learning Applicatipon------------")

    print("Play predictor application using K Nearest Knighbor algoritham")

    MarvellousPlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()
"""







"""
from sklearn import tree

def PlayPredictorCasestudy(whether,temprature):
    # 3 entries
    # Sunny    - 1
    # Overcast - 2
    # Rainy    - 3

    # temprature are
    # Cold   - 5
    # Mild   - 6
    # Hot    - 7

    # Labels 
    # Yes - 1
    # No -  0

    # 1 Load the data
    Features = [[1,7],[1,7],[2,7],[3,6],[3,5],[3,5],[2,5],[1,6],[1,5],[3,6],[1,6],[2,6],[2,7],[3,6],[3,6],[3,5],[3,5],[2,5],[1,6],[1,5],[3,6],[1,6],[1,7],[1,7],[2,7],[3,6],[3,5],[2,5],[1,6],[1,5]]    

    Labels = [0,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1]

    #Deside the Machine learning algorithem
    obj = tree.DecisionTreeClassifier()

    # Perform the treanning of model
    obj = obj.fit(Features, Labels)

    # perform of testing 
    ret = (obj.predict([[whether,temprature]]))
    if ret == 1:
        print("Now you are play.")
    else:
        print("You not play.")

def main():
    print("-------------Play Predictor Case Study------------")

    print("Please enter the whether (Sunny / Overcast / Rainy)")
    whether = input()

    if whether.lower() == "sunny":
        whether = 1
    elif whether.lower() == "overcast":
        whether = 2
    elif whether.lower() == "rainy":
        whether = 3
    else:
        print("Invalid type of whether")
        exit()

    print("Please enter the temprature (Cold / Mild / Hot)")
    temprature = input()

    if temprature.lower() == "cold":
        temprature = 5
    elif temprature.lower() == "mild":
        temprature = 6
    elif temprature.lower() == "hot":
        temprature = 7
    else:
        print("Invalid type of temprature")
        exit()

    PlayPredictorCasestudy(whether,temprature)

if __name__ == "__main__":
    main()

"""