import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

INPUT_PATH = "breast-cancer-wisconsin.csv"
OUTPUT_PATH = "breast-cancer-wisconsin.csv"

HEADERS = ["CodeNumber","ClumpThickness","UniformityCellSize","UniformityCellShape","MarginalAdhesion","SingleEpithelialCellSize","BareNuclei","BlandChromatin","NormalNucleoli","Mitoses","CancerType"]

def read_data(path):
    data = pd.read_csv(path)
    return data

def get_headers(dataset):
    return dataset.columns.values

def add_headers(dataset, headers):
    dataset.columns = headers
    return dataset

def data_file_to_csv():

    headers = ["CodeNumber","ClumpThickness","UniformityCellSize","UniformityCellShape","MarginalAdhesion","SingleEpithelialCellSize","BareNuclei","BlandChromatin","NormalNucleoli","Mitoses","CancerType"]

    dataset = read_data(INPUT_PATH)

    dataset = add_headers(dataset,headers)

    dataset.to_csv(OUTPUT_PATH,index=False)
    print("File saved...!")

def split_dataset(dataset,train_percentage, feature_headers, target_header):

    train_x, test_x, train_y, test_y = train_test_split(dataset[feature_headers],dataset[target_header],train_size = train_percentage)
    return train_x, test_x, train_y, test_y

def handel_missing_values(dataset, missing_value_header, missing_label):
    return dataset[dataset[missing_value_header] != missing_label]

def random_forest_classifier(features, target):
    clf = RandomForestClassifier()
    clf.fit(features, target)
    return clf

def dataset_statistics(dataset):
    print(dataset.describe())

def main():
    dataset = pd.read_csv(OUTPUT_PATH)

    dataset_statistics(dataset)

    dataset = handel_missing_values(dataset, HEADERS[6], '?')

    train_x, test_x, train_y, test_y = split_dataset(dataset,0.7,HEADERS[1:-1],HEADERS[-1])

    print("Train_x Shape :: ",train_x.shape)
    print("Train_y Shape :: ",train_y.shape)
    print("Train_x Shape :: ",test_x.shape)
    print("Train_y Shape :: ",test_y.shape)

    trained_model = random_forest_classifier(train_x,train_y)
    print("Trained model :: ",trained_model)
    predictions = trained_model.predict(test_x)

    for i in range(0,205):
        print("Actual outcome ::{} and Predicted Outcome :: {}".format(list(test_y)[i],predictions[i]))

        print("Train Accuracy ::",accuracy_score(train_y, trained_model.predict(train_x)))
        print("Test Accuracy :: ",accuracy_score(test_y,predictions))
        print("confusion_matrix :: ",confusion_matrix(test_y, predictions))

if __name__ == "__main__":
    main()
