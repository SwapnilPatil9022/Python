# ------------- Links Extractor using Web Scrapping ----------------"""

import os
import bs4
import requests
from sys import *

def LinksDisplay(URL):
    res = requests.get(URL)
    print(type(res))

    soup = bs4.BeautifulSoup(res.text,'lxml')
    print(type(res))

    links = soup.find_all('a', href = True)

    return links 

def main():
    print("------ Links Extractor using Web Scrapping By Swapnil Patil ------")

    print("Application name : "+argv[0])

    if (len(argv) == 2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("This script is used to fetch links from wikipedia file")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("Usage : ApplicationName")
            exit()

    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    arr = LinksDisplay(url)

    print("Links are ")

    for element in arr:
        if "#" not in element['href']:
            print(element['href'])

if __name__ == "__main__":
    main()























"""
#  ------------ Auto Image Downloader using Web Scrapping ---------------

#=================================================
# Required Python Packages
#=================================================
from bs4 import *
import requests
import os

#=================================================
# Function name : folder_create
# Description : folder_create function create a current directory
# Author : Swapnil Ashok Patil
# Date : 15/01/2023
#=================================================
def folder_create(images):
    try:
        folder_name = input("Enter Folder Name :-")
        os.mkdir(folder_name)
    except:
        print("Folder Exist with that name!")
        folder_create()

    download_images(images,folder_name)

#=================================================
# Function name : download_images
# Description : download_images function from download the Images.
# Author : Swapnil Ashok Patil
# Date : 15/01/2023
#=================================================
def download_images(images,folder_name):
    count = 0

    print(f"Total {len(images)} Image Found!")

    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image["data-srcset"]

            except:
                try:
                    image_link = image["data-src"]
                except:
                    try:
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]

                        except:
                            pass


            try:
                r = requests.get(image_link).content
                try:
                    r = str(r,'utf-8')

                except UnicodeDecodeError:
                    with open(f"{folder_name}/images{i+1}.jpj","wb+")as f:
                        f.write(r)

                count += 1

            except:
                pass

        if count == len(images):
            print("All Images Downloaded!")
        else:
            print(f"Total {count} Images download Out of {len(images)}")

#=================================================
# Function name : main
# Description : Main function from where execution starts
# Author : Swapnil Ashok Patil
# Date : 15/01/2023
#=================================================
def main():
    print("------Auto_Image_Downloader_using_Web_Scrapping_By Swapnil_Patil-------")

    print("Application name : Auto Image Downloader")

    url = ("https://www.amazon.in/s?k=laptop&crid=13FMWB6PBBAUY&sprefix=laptop%2Caps%2C360&ref=nb_sb_noss_1")

    r = requests.get(url)

    soup = BeautifulSoup(r.text,'html.parser')

    images = soup.findAll('img')

    folder_create(images)

#=================================================
# Application starter
#=================================================
if __name__ == "__main__":
    main()
"""























"""
# import os
# import time 
# import psutil
# import urllib2
# import smtplib
# import schedule
# from sys import *
# from email.mime.text import MIMEText
# form email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart

# def is_connected():
#     try:
#         urllib2.urlopen('http://216.58.192.142',timeout = 1)
#         return True
#     except urllib2.URLError as err:
#         return False

# def MailSender(filename,time):
#     try:
#         fromaddr = "swapnilpatil46118@gmail.com"
#         toaddr = "devapukale929@gmail.com"

#         msg = MIMEMultipart()

#         msg['From'] = fromaddr

#         msg['To'] = toaddr

#         body = """
#         Hello %s,
#         Welcome.
#         Please find attached document which contains Log of Running process.
#         Log file is created at : %s 

#         This is auto gennerated mail.

#         Thanks & Regards,
#         Swapnil Ashok Patil
#         """%(toaddr,time)

#         Subject = """

#         Process log generated at : %s
#         """%(time)

#         msg['Subject'] = Subject

#         msg.attach(MIMEText(body,'plain'))

#         attachment = open(filename,"rb")

#         p = MIMEBAse('application','octel-stream')

#         p.set_payload((attachment).read())

#         encoders.encode_base64(p)

#         p.add_header('Content-Disposition',"attachment; filename= %s" %filename)

#         msg.attach(p)

#         s = smtplib.SMTP('smtp.gmail.com',587)

#         s.starttls()

#         s.login(fromaddr,"xvfxeadltnyzbnoj")

#         text = msg.as_string()

#         s.sendmail(fromaddr,toaddr,text)

#         s.quit()

#         print("Log file successfully send to mail")

#     except Exception as E:
#         print("Unable to send mail.",E)

# def ProcessLog(log_dir = 'Marvellous'):
#     listprocess = []

#     if not os.path.exists(log_dir):
#         try:
#             os.mkdir(log_dir)
#         except:
#             pass


#     separator = "-"*80

#     log_path = os.path.join(log_dir,"MarvellousLog%s.log" %(time.ctime()))
#     f = open(log_path, 'w')
#     f.write(separator + "\n")
#     f.write("Process Logger : "+time.ctime() + "\n")
#     f.write(separator + "\n")
#     f.write("\n")

#     for proc in psutil.process_iter():
#         try:
#             pinfo = proc.as_dict(attrs=['pid','name','username'])
#             vms = proc.memory_info().vms/(1024*1024)
#             pinfo['vms'] = vms
#             listprocess.append(pinfo);
#         except (psutil..NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
#             pass

#     for elements in listprocess:
#         f.write("%s\n % element")

#     print("Log file is successfully generated at location %s",%(log_path))

#     connected = is_connected()

#     if connected:
#         startTime = time.time()
#         MailSender(log_path,time.ctime())
#         endTime = time.time()

#         print('Took %s secounds to send mail' %(endTime - startTime))
#     else:
#         print("There is no internet connect")

# def main():
#     print("-----Process Logger by Swapnil Patil-----")

#     print("Application name : "+argv[0])

#     if(len(argv) != 2):
#         print("Error : Invalid number of arguments")
#         exit()

#     if (argv[1] == "-h") or (argv[1] == "-H"):
#         print("This Script is used log record of running processess")
#         exit()

#     if (argv[1] == "-u") or (argv[1] == "-U"):
#         print("Usage : Application_Name Absolutepath_of_Directory")
#         exit()

#     try:
#         schedule.every(int(argv[1])).minutes.do(ProcessLog)
#         while True:
#             schedule.run_pending()
#             time.sleep(1)
#     except ValueError:
#         print("Error : Invalid datatype of input")

#     except Exception as E:
#         print("Error : Invalid input",E)

# if __name__ == "__main__":
#     main()

"""






















"""
"""
import pandas as pd
import matplotlib.pyplot as plt

def Matplotlib():
    excel_file = 'Marvellous.xlsx'
    data = pd.read_excel(excel_file)

    print("All data from excel file")
    print(data)

    print("First 5 rows from file")
    print(data.head())

    print("First 4 rows from file")
    print(data.head(4))

    print("First 3 rows from file")
    print(data.tail(3))

    print(data.shape)

    Sorted_data = data.sort_values(['Name'],ascending = False)
    print("Sorted data")
    print(Sorted_data)

    data['Age'].plot(kind="hist")
    plt.show()

    data['Age'].plot(kind="barh")
    plt.show()

def main():
    Matplotlib()

if __name__ == "__main__":
    main()

"""






















"""
# Requierd library's
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def HeadBrainPredictor():
    # Load the data
    data = pd.read_csv("HeadBrain.csv")

    print("Size if data set",data.shape)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    # Least square method
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    n = len(X)

    numerator = 0
    denomenator = 0

    # Equation of line is y = mx + c
    for i in range(n):
        numerator += (X[i] - mean_x)*(Y[i] - mean_y)
        denomenator += (X[i] - mean_x)**2

    m = numerator / denomenator

    c = mean_y - (m * mean_x)

    print("Slope of Regression line is : ",m)
    print("Y intercept of Regression line is : ",c)

    max_x = np.max(X)+100
    min_x = np.min(X)-100

    # Display plotting of above points
    x = np.linspace(min_x,max_x,n)

    y = c + m * x 

    plt.plot(x,y,color = 'blue',label = 'Regression Line')

    plt.scatter(X,Y,color = 'orange',label = 'scatter plot')

    plt.xlabel('Head size in cm3')

    plt.ylabel('Brain weight in gram')

    plt.legend()
    plt.show()

    # Findout goodness of fit of fit ie R Square
    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m * X[i]
        ss_t += (Y[i] - mean_y)**2
        ss_r += (Y[i] - y_pred)**2

    r2 = 1 - (ss_r/ss_t)

    print(r2)

def main():
    print("-------- Head Brain Case Study by Swapnil Patil---------")

    print("Supervised Machine Learning")

    print("Linear Regression on Head and Brain size data set")

    HeadBrainPredictor()

if __name__ == "__main__":
    main()
"""





















"""
import pandas as pd
from sklearn import tree
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def MArvellous(path):
    sp = pd.read_csv(path)
    print(sp)

    X = sp['Head Size(cm^3)'].values
    Y = sp['Brain Weight(grams)'].values

    X = X.reshape((-1,1))

    n = len(X)
    print(n)    

    reg =LinearRegression()

    reg = reg.fit(X,Y)

    model = reg.predict(X)

    r2 = reg.score(X,Y)

    print(r2)

def main():
    path = "HeadBrain.csv"
    MArvellous(path)

if __name__ == "__main__":
    main()

"""


















"""
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn import tree

def marvellous(path):
    dataset = pd.read_csv(path)
    print(dataset)

    X = dataset['Head Size(cm^3)'].values
    Y = dataset['Brain Weight(grams)'].values

    X = X.reshape((-1,1))

    n = len(X)
    print(n)

    reg = LinearRegression()

    reg = reg.fit(X,Y)

    y_pred = reg.predict(X)

    r2 = reg.score(X,Y)

    print(r2)

def main():
    path = "HeadBrain.csv"
    marvellous(path)

if __name__ == "__main__":
    main()
"""























"""
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def marvellous(path):
    df = pd.read_csv(path)
    print(df)

    le  = preprocessing.LabelEncoder()

    Wether = df.Whether
    whether_encoder = le.fit_transform(Wether)
    print(whether_encoder)

    temp = df.Temperature
    temp_encoded = le.fit_transform(temp)
    print(temp_encoded)

    label = df.Play
    label = le.fit_transform(label)
    print(label)

    features = list(zip(whether_encoder,temp_encoded))

    model = KNeighborsClassifier()

    Result = model.fit(features,label)

    predicted = Result.predict([[0,1]])

    print(predicted)

    if predicted == 0:
        print("No Play")
    else:
        print("Play")


def main():
    path = "PlayPredictor.csv"

    marvellous(path)

if __name__ == "__main__":
    main()
"""























"""
import bs4
import requests

def Web_Scrapping(url_path):
    res = requests.get(url_path)

    print(type(res))

    # print(res.text)

    soup = bs4.BeautifulSoup(res.text)
    print(type(soup))

    title = soup.select('title')
    print(title[0].getText())

    print("Title is ")
    print(title[0].getText())

    arr = soup.select(".mw-headline")

    for element in arr:
        print(element.text)

def main():
    URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    Web_Scrapping(URL)

if __name__ == "__main__":
    main()

"""
















"""
# ----------- Play-Predictor casestudy using DecisionTree algoritham---------------
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

"""























"""
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import tree

def Play_Predictor_DT(data_path):
    sp = pd.read_csv(data_path)
    print(sp)

    features = ["Whether","Temperature"]
    print(features)
    label = ["Play"]
    print(label)

    coder = preprocessing.LabelEncoder()

    whether = sp.Whether
    whether_encoder = coder.fit_transform(whether)
    print(whether_encoder)

    temprature = sp.Temperature
    temp_encoder = coder.fit_transform(temprature)
    print(temp_encoder)

    label = sp.Play
    label = coder.fit_transform(label)
    print(label)

    features = list(zip(whether_encoder,temp_encoder))

    model = tree.DecisionTreeClassifier()

    model.fit(features,label)

    pred = model.predict([[2,1]])

    print(pred)



def main():
    Play_Predictor_DT("PlayPredictor.csv")

if __name__ == "__main__":
    main()
"""























"""
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def marvellous(data_path):
    # Load the dataset
    df = pd.read_csv(data_path, index_col=0)
    print(df)
    print(len(df))
    print(type(df))

    # clean , prepare and manipulate the data
    Feature_names = ["Whether","Temperature"]
    # print(Feature_names)
    label = ["Play"]
    # print(label)

    whether = df.Whether
    temprature = df.Temperature
    play = df.Play

    # Encoding the data
    le = preprocessing.LabelEncoder()

    whether_encoded = le.fit_transform(whether)
    print(whether_encoded)
    temp_encoded = le.fit_transform(temprature)
    print(temp_encoded)
    label = le.fit_transform(play)
    print(label)

    features = list(zip(whether_encoded,temp_encoded))

    classifier = KNeighborsClassifier()

    classifier.fit(features,label)

    Predictied = classifier.predict([[0,1]]) 
    print(Predictied)

def main():
    marvellous("PlayPredictor.csv")

if __name__ == "__main__":
    main()
"""


















"""
import numpy as np 
import pandas as pd

data = (111,1112,1131,41,511)
df = pd.DataFrame(data)

writer = pd.ExcelWriter("Sp1.xlsx",engine="xlsxwriter")
df.to_excel(writer,sheet_name = "Sheet1")
writer.save()
"""
















"""
import pandas as pd
import numpy as np

# data = np.array(['a','b','c','d'])
# s = pd.Series(data)
# print(s[0])

# data = np.array(['a','b','c','d'])
# s = pd.Series(data,index=[100,101,102,103])
# print(s[102])

# data = {'a' : 0.1,'b' : 1.1,'c' : 2.1}
# s = pd.Series(data)
# print(s)

# data = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# print(data['a'])

data = [{'Name' : 'PPA','Duration' : 3,'Fees' : 10500},{'Name' : 'LB','Duration' : 3,'Fees' : 10800},{'Name' : 'Python','Duration' : 3,'Fees' : 20500}]
df = pd.DataFrame(data)
print(df)

writer = pd.ExcelWriter('sp.xlsx',engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1')

writer.save()
"""














"""
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
"""


















"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def MarvellousHeadBrianPredictor():
    # Load data
    data = pd.read_csv("HeadBrain.csv")

    print("Size if data set",data.shape)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    X = X.reshape((-1,1))

    n = len(X)

    reg = LinearRegression()

    reg = reg.fit(X,Y)

    y_pred = reg.fit(X,Y)

    y_pred = reg.predict(X)

    print(y_pred)

    print(y_pred)

    r2 = reg.score(X,Y)

    print(r2)


def main():
    MarvellousHeadBrianPredictor()

if __name__ == "__main__":
    main()
"""























"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():

    # Load data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Value of Independent of variables X :",X)
    print("Value of Dependent of variables Y :", Y)

    # Lest square method
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("Mean of Independent variable x : ",mean_x)
    print("Mean of Dependent variable y : ",mean_y)
    n = len(X)

    numerator = 0
    denomenator = 0

    # Equation of line is y = mx + c

    for i in range(n):
        numerator += (X[i] - mean_x)*(Y[i] - mean_y)

        denomenator += (X[i] - mean_x)**2

    m = numerator / denomenator

    # c = y' - mx'

    c = mean_y - (m * mean_x)

    print("Slope of Regression line is : ",m)  # 0.4
    print("Y intercept of Regression lilne is :",c)  # 2.4

    # Display plotting of above points
    x = np.linspace(1,6,n)

    y = c + m * x

    plt.plot(x,y, color='black', label='Regression Line')
    plt.scatter(X,Y, color='red', label='scatter plot')

    plt.xlabel('X - Independent Variable')
    plt.ylabel('Y - Dependent Variable')

    plt.legend()
    plt.show()

    # Findout goodness of fit ie R Sqaure
    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m * X[i]
        ss_t += (Y[i] - mean_y) ** 2
        ss_r += (Y[i] - y_pred) ** 2

    r2 = 1 - (ss_r/ss_t)

    print("Goodness of fit using R2 method is ",r2)

def main():
    print("Supervised Machine Learning")

    print("Linear Regression")

    MarvellousPredictor()

if __name__ == "__main__":
    main()

"""




















"""
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def Mar(data_path):
    data = pd.read_csv(data_path, index_col = 0)

    print("Size of actual dataset ", len(data))

    feature_name = ['Whether','Temperature']

    print("Names os feature_names", feature_name)

    whether = data.Whether
    Temperature = data.Temperature
    Play = data.Play

    le = preprocessing.LabelEncoder()

    wether_encoded = le.fit_transform(whether)
    print(wether_encoded)
    temp_encoded = le.fit_transform(Temperature)
    print(temp_encoded)
    label = le.fit_transform(Play)

    features = list(zip(wether_encoded,temp_encoded))

    model = KNeighborsClassifier(n_neighbors = 3)

    model.fit(features,label)

    Predicted = model.predict([[0,2]])  # : overcast    2:Mild
    print(Predicted)

    if Predicted:
        print("Play")
    else:
        print("Not play")

def main():
    Mar("PlayPredictor.csv")

if __name__ == "__main__":
        main()

"""























"""
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plot

def Mar(data_path):
    data = pd.read_csv(data_path, index_col = 0)

    print("Size of actual dataset ", len(data))

    feature_name = ['Whether','Temperature']

    print("Names os feature_names", feature_name)

    X = data[feature_name]

    Y = data.Play

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 1/2)

    print("Size of Tranning dataset", len(X_train))

    print("Size on Testing dataset ", len(X_test))

def main():
    Mar("PlayPredictor.csv")


if __name__ == "__main__":
    main()

"""



















"""
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Assigning feature and label variables
# First Feature
wether = ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']

# Secound Feature
temp = ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

# Label or target varible
play = ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

# Import LabelEncoder
from sklearn import preprocessing

# Crating labelEncoder
le = preprocessing.LabelEncoder()

# Converting sting labels into numbers.
wether_encoded = le.fit_transform(wether)

print(wether_encoded)

# Converting string labels into numbers
temp_encoded = le.fit_transform(temp)
label = le.fit_transform(play)

print(temp_encoded)

# combining wether and temp into single listof tuples
features = list(zip(wether_encoded,temp_encoded))

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors = 3)

# Train the model using the traning sets
model.fit(features,label)

# Predict Output
predicted = model.predict([[0,2]])  # 0: Overcast, 2 : Mild
print(predicted)


"""















"""

def MarvellousPlayPredictior(data_path):
    data = pd.read_csv(data_path, index_col=0)

    print("Size of actual dataset is :",len(data))




def main():
    MarvellousPlayPredictior("PlayPredictor.csv")

if __name__ == "__main__":
    main()
"""












"""
# import numpy as np
# import pandas as pd
# from sklearn import metrics
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
"""







"""
from sklearn import tree
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a,b):
    return distance.euclidean(a,b)

class MarvellousKNN:
    def fit(self,TraningData,TraningTarget):
        self.TraningData = TraningData
        self.TraningTarget = TraningTarget

    def predict(self,TestData):
        predictions = []
        for row in TestData:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self,row):
        bestdistance = euc(row,self.TraningData[0])
        bestindex = 0
        for i in range(1,len(self.TraningData)):
            dist = euc(row,self.TraningData[i])
            if dist < bestdistance:
                bestdistance = dist
                bestindex = i
        return self.TraningTarget[bestindex]

def ML():
    Dataset = load_iris()

    Data = Dataset.data
    Target = Dataset.target

    Data_train, Data_test,Target_train, Target_test = train_test_split(Data,Target, test_size = 0.5)
    print("TRANING DATA :",Data_train)
    print("TEST DATA :",Data_test)
    print("TRANING DATA :",Data_train)
    print("TEST DATA :",Target_test)

    classifier = MarvellousKNN()

    classifier.fit(Data_train, Target_train)

    Predictions = classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test, Predictions)

    return Accuracy

def main():
    ret = ML()
    print("Result is : ",ret * 100)

if __name__ == "__main__":
    main()
"""
























"""
    -------------------- Supervised Machine Learning -------------------------
    ------------- Accuracy Calculation with Decision Tree --------------------
                                    &
    ------------------------ K Nearest Neighbour -----------------------------

    * In this application we train iris data set with Decision Tree algoritham and k Nearest Neighbour algoritham
    * We divide iris data set into two equal as training data and test data.
    * We apply training on training data and predict the data result on test data.
    * We calculate accuracy of both the algorithams by applaying of test data.

    - Consider below characteristics of machine learning application : 

    classifier      : Decision Tree & K Nearst Neighbour
    Dataset         : Iris Dataset
    Features        : Sepal Width, Sepal length, petal Width, petal Length
    Labels          : Versicolor , setosa , Virginica   
    Traning Dataset :  75 Enteris
    Testing Datset  :  75 Enteris
    ------------------------------------------------------------------------
"""
"""
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def MarvellousCalculateAccuracyDecisionTree():
    iris = load_iris()

    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data,target,test_size = 0.5)

    # Using DecisionTree algoritham
    classifier = tree.DecisionTreeClassifier()

    classifier.fit(data_train,target_train)

    Predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, Predictions)

    return Accuracy
 
def MarvellousCalculateAccuracyKNeighbor():
    iris = load_iris()

    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data,target,test_size = 0.5)

    # Using KNN algoritham
    classifier = KNeighborsClassifier()

    classifier.fit(data_train,target_train)

    Predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, Predictions)

    return Accuracy

def main():
    Accuracy = MarvellousCalculateAccuracyDecisionTree()
    print("Accuracy of classification algorithm with Decision Tree classifier is :",Accuracy*100,"%d")

    Accuracy = MarvellousCalculateAccuracyKNeighbor()
    print("Accuracy of classification algorithm with K Neighbour classifier is :",Accuracy*100,"%d")

if __name__ == "__main__":
    main()
"""













"""


from sklearn.datasets import load_iris
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from scipy.spatial import distance

def ecu(a,b):
    return distance.euclidean(a,b)

class MarvellousKNeigbhoursClassifier:

    def fit(self,trainningdata, trainingtarget):
        self.TraningData = trainningdata
        self.TrainingTarget = trainingtarget

    def closest(self,row):
        minimumdistance = ecu(row,self.TraningData[0])
        minimumindex = 0

        for i in range(1,len(self.TraningData)):
            Distance = ecu(row, self.TraningData[i])
            if Distance < minimumdistance:
                minimumdistance = Distance
                minimumindex = i

        return self.TraningData[minimumindex]

    def predict(self, TestData):
        Predictions = []
        for value in TestData:
            result = self.closest(value)
            Predictions.append(result)

        return Predictions

def ML():
    Dataset = load_iris()

    Data = Dataset.data
    Target = Dataset.target

    Data_train, Data_test,Target_train, Target_test = train_test_split(Data,Target, test_size = 0.5)

    classifier = MarvellousKNeigbhoursClassifier()

    classifier.fit(Data_train, Target_train)

    Predictions = classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test, Predictions)

    return Accuracy

def main():
    ret = ML()
    print("Result is : ",ret * 100)

if __name__ == "__main__":
    main()
"""


























"""
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def MarvellousKNeighborsClassifier():
    Dataset = load_iris()

    Data = Dataset.data
    Target = Dataset.target

    Data_train, Data_test,Target_train, Target_test = train_test_split(Data,Target, test_size = 0.5)

    classifier = KNeighborsClassifier()

    classifier.fit(Data_train, Target_train)

    Predictions = classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test, Predictions)

    return Accuracy

def main():
    ret = MarvellousKNeighborsClassifier()
    print("Result is : ",ret * 100)

if __name__ == "__main__":
    main()
"""





















"""
from sklearn.datasets import load_iris

iris = load_iris()

print("Features name")
print(iris.feature_names)

print("Target names")
print(iris.target_names)

for i in range(len(iris.target)):
    print("ID : %d, Label %s, Feature : %s" % (i,iris.data[i],iris.target[i]))

"""















"""
import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()

print("Features name")
print(iris.feature_names)

print("Target names")
print(iris.target_names)

test_index = [1,51,101]

train_target = np.delete(iris.target,test_index)
train_data = np.delete(iris.data,test_index,axis = 0)

test_target = iris.target[test_index]
test_data = iris.data[test_index]

classifier = tree.DecisionTreeClassifier()

classifier.fit(train_data, train_target)

print("Values that we removed for testing")
print(test_target)

print("Result of testing")
print(classifier.predict(test_data))

"""
















"""
from sklearn import tree
Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 
Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

classifier = tree.DecisionTreeClassifier()

classifier.fit(Features, Labels)

ret = classifier.predict([[90,0],])

if (ret == 2):
    print("tennis")
else:
    print("Cricket")
"""


















"""
import urllib3

http = urllib3.PoolManager()

url = 'https://www.python.org/'

resp = http.request('GET', url)
print(resp.data.decode('utf-8'))

"""







"""
#  

# read the data from the URL and print it
#
import urllib3

def main():
# open a connection to a URL using urllib2
   webUrl =urllib3.PoolManager("https://www.youtube.com/user/guru99com")
  
#get the result code and print it
   print +str(webUrl()) 
  
# read the data from the URL and print it
   data = webUrl.read()
   print(data)
 
if __name__ == "__main__":
    main()


"""







"""
import urllib.request

def is_connected():
    # try:
    urllib.request.urlopen("https://www.python.org/")
    # webUrl = urllib2.urlopen("https://www.python.org/")

def main():
    is_connected()

if __name__ == "__main__":
    main()
"""


"""
import urllib3
from bs4 import BeautifulSoup

url = 'http://www.thefamouspeople.com/singers.php'

http = urllib3.PoolManager()
response = http.request('GET', url)
soup = BeautifulSoup(response.data.decode('utf-8'))

"""








"""
import os
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

def iris():
    iris = load_iris()

    print("Features name")
    print(iris.feature_names)

    print("Target name")
    print(iris.target_names)

    test_index = [1,51,101]

    train_target = np.delete(iris.target,test_index)
    train_data = np.delete(iris.data, test_index, axis = 0)

    test_target = iris.target(test_index)
    test_data = iris.data(test_index)

    classifier = tree.DecisionTreeClassifier()

    classifier.fit(train_data,train_target)

    print("Value removed")
    print(test_target)

def main():
    iris()

if __name__ == "__main__":
    main()



"""


















"""
from sklearn import tree


Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 
Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

obj = tree.DecisionTreeClassifier()

obj = obj.fit(Features, Labels)

First = int(input("Enter the weigth\n"))
Secoound = int(input("Enter the surface\n"))

ret = (obj.predict([[First,Secoound],]))

if (ret == 1):
    print("Criket")
else:
    print("Tennnis")
"""

















"""
from sklearn import tree

# Load the dataset
# Rough     1
# Smooth    0

# Tennis    1
# Criket    2

Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 
Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

#Deside the Machine learning algorithem
obj = tree.DecisionTreeClassifier()

# 
obj = obj.fit(Features, Labels)

print(obj.predict([[97,0],[35,1]]))
"""

















"""
import os
import re
import requests
from sys import*
from urllib.parse import urlparse

def is_downloadable(url):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content_type')

    if 'text' in content_type.lower():
        return False    
    if 'html' in content_type.lower():
        return False

    return True

def get_filename_from_cd(cd):
    a = urlparse(cd)
    return os.path.basename(a.path)

def Download_Data(url):
    allowed = is_downloadable(url)

    if allowed:
        try:
            res = requests.get(url, allow_redirects = True)
            
            filename = get_filename_from_cd(url)
            fd = open(filename,"wb")

            for buffer in res.iter_content(1024):
                fd.write(buffer)

            fd.close()
            return True

        except Exception as E:
            return False    
    else:
        return False

def main():
    print("Application name : "+argv[0])

    if (len(argv) == 2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("This Script is used to download file")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("Usage : ApplicationName")
            exit() 

    url = 'https://www.google.com/favicon.ico'

    result = Download_Data(url)

    if result:
        print("File successfully downloaded")
    else:
        print("Failed to download")

if __name__ == "__main__":
    main() 

"""























"""
import re
from sys import*
import webbrowser
from urllib.request import urlopen

def is_connected():
    try:
        urlopen('http://google.com')
        return True
    except Exception as err:
        return False

def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*/(/), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url

def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            url = Find(line)
            for str in url:
                webbrowser.open(str, new = 2)

def main():
    print("Application name : "+argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of argument")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used open URL which are written in one file")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName Name_Of_File")
        exit()

    try:
        connected = is_connected()

        if connected:
            WebLauncher(argv[1])
        else:
            print("Unable to connect to internet...")

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()
"""























"""

"""
#            --------- Automation using python -----------
 #   Automation script which accept directory name from user and remove duplicate files from that directory.
"""

#=================================================
# Required python Packages
#=================================================
import os
import hashlib
from sys import*
import time

#=================================================
# Function name : DeleteFiles
# Description : This function is work Duplicate file remove
# Author : Swapnil Ashok Patil
# Date : 04/01/2023
#=================================================
def DeleteFiles(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values()))

    icnt = 0

    if len(results) > 0:
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    os.remove(subresult)
            icnt = 0
    else:
        print("No Duplicate file found.")


#=================================================
# Function name : hashfile
# Description : This hashfile function read the data and search checksum in directory.
# Author : Swapnil Ashok Patil
# Date : 04/01/2023
#=================================================
def hashfile(path, blocksize = 1024):
    fd = open(path,'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()

    return hasher.hexdigest()


#=================================================
# Function name : FindDuplicate
# Description : FindDuplicate function is find the duplicate files from directory
# Author : Swapnil Ashok Patil
# Date : 04/01/2023
#=================================================
def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}
    if exists:
        #---Travel the directory,subdirectory and files----
        for dirName, subdirs, fileList in  os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path) 
            
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid path")

#=================================================
# Function name : PrintResult
# Description : PrintResult function is find the duplicates files
# Author : Swapnil Ashok Patil
# Date : 04/01/2023
#=================================================
def PrintResult(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values())) 

    if len(results) > 0:
        print("Duplicates Found : ")
        print("The following files are Duplicate....")

        for result in results:
            for subresult in result:
                print("\t\t%s"% subresult)
    else:
        print("No duplicate file found")

#=================================================
# Function name : main
# Description : Main function from where execution starts
# Author : Swapnil Ashok Patil
# Date : 04/01/2023
#=================================================
def main():
    print("--------Search Duplicate file and checksum from that Directory using Automation script--------")

    print("Application name : " +argv[0])

    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used to traverse specific directory and remove Duplicate files")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName Absolutepath_of_Directory Extension")
        exit()

    try:
        arr = {}
        startTime = time.time()
        arr = FindDuplicate(argv[1])
        PrintResult(arr)
        DeleteFiles(arr)
        endTime = time.time()

        print("Took %s secound to evaluate."% (endTime - startTime))

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

#=================================================
# Application starter
#=================================================
if __name__ == "__main__":
    main()

"""


























"""
"""
#            --------- Automation using python -----------
  # Automation script which accept directory name from user and display all names and checksum of duplicate files from that directory.
"""

from sys import*
import os
import hashlib

def hashfile(path, blocksize = 1024):
    fd = open(path,'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()

    return hasher.hexdigest()

def DisplayChecksum(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName, subdirs, fileList in  os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path) 
                print(path)
                print(file_hash)
                print(' ')

def printDuplicate(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values())) 

    if len(results) > 0:
        print("Duplicates Found : ")

        print("The following files are identical")

        icnt = 0
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    print("\t\t%s"% subresult)
    else:
        print("No duplicate file found")

def main():
    print("--------Search Duplicate file and checksum from that Directory using Automation script--------")

    print("Application name : " +argv[0])

    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used to traverse specific directory and display size of files")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName Absolutepath_of_Directory Extension")
        exit()

    try:
        arr = DisplayChecksum(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()

"""


























"""

"""
 #                   Automation using python
  #  Automation script which accept directory name from user and display all names of duplicate files from that directory.
"""

from sys import*
import os
import hashlib

def hashfile(path, blocksize = 1024):
    fd = open(path,'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()

    return hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}
    if exists:
        for dirName, subdirs, fileList in  os.walk(path):
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path) 
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups 
    else:
        print("Invalid path")

def printDuplicate(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values())) 

    if len(results) > 0:
        print("Duplicates Found : ")

        print("The following files are identical")

        icnt = 0
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    print("\t\t%s"% subresult)
    else:
        print("No duplicate file found")

def main():
    print("--------Search Duplicate file from Directory using Automation script--------")

    print("Application name : " +argv[0])

    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used to traverse specific directory and display size of files")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName Absolutepath_of_Directory Extension")
        exit()

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        printDuplicate(arr)

    except ValueError:
        print("Error : Invalid datatype of input")

if __name__ == "__main__":
    main()

"""




















"""

import numpy as np 
import pandas as pd
from sklearn import metrics
from sklearn import preprocessing

df = pd.read_csv("housing_data.csv")
print(df)


n = len(df)
print(n)

X = df['area (in cm)'].values
Y = df['price in lakhs'].values
mean_x = np.mean(X)
mean_y = np.mean(Y)
print(mean_x)
print(mean_y)

nemerator = 0
denomenator = 0
for i in range(n):
    nemerator += (X[i] - mean_x)*(Y[i] - mean_y)
    denomenator += (X[i] - mean_x)**2
m = nemerator / denomenator
c = mean_y - (m * mean_x)

print(m, c)

import matplotlib.pyplot as plt

max_x = np.max(X) + 100
min_x = np.min(x) - 100

x = np.linspace(min_x, max_x, 1000)
y = c + m * X_test

plt.plot(x,y, color = 'blue', label = 'Regression Line')


plt.Xlable('Area (in cm)')
plt.ylable('price in lakhs')
plt.legend()
plt.show()
"""


















"""

le = preprocessing.LabelEncoder()

df1 = df.apply(le.fit_transform)
print(df1)

X = df[['outlook','temperature','humidity','windy']]
Y = df['play']

from sklearn import tree 
cd = tree.DecisionTreeClassifier(criterion = 'entropy')
cd = cd.fit(X,Y)

de = tree.plot_tree(cd)
print(de)

"""









"""
import pandas as pd
df = pd.read_csv("iris_null_values.csv")
print(df)

df.isnull().sum()

fd1 = df[df['sepal.length'].isnull()]
print(fd1)

fd2 = df[df['sepal.width'].isnull()]
print(fd2)

fd3 = df.fillna('default')
print(fd3)

fd4 = df.isnull()
print(fd4)

fd5 = df.notnull()
print(fd5)

fd6 = df.dropna()
print(fd6)
"""













"""
import pandas as pd
df = pd.read_csv("iris.csv")

print(df)

import matplotlib.pyplot as plt
plt.scatter(df['sepal.length'],df['sepal.width'])
plt.xlabel('sepal.length')
plt.ylabel('sepal.width')
plt.show()

"""

















"""
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

fd = load_iris()

Data = fd.data
Target = fd.target

Data_train,Data_test,Target_train,Target_test = train_test_split(Data, Target, test_size = 0.5)

classifier = KNeighborsClassifier()
classifier.fit(Data_train,Target_train)

prediction = classifier.predict(Data_test)

Accuracy  = accuracy_score(Target_test,prediction)

print("Accuracy is",Accuracy * 100)
"""


















"""
import pandas as pd

fd  = pd.read_csv("iris.csv")
print(fd)
"""
















"""
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def MarvellousKNeighbourClassifier():
    # 1. Load the data 
    Dataset = pd.read_csv("iris.csv")
    print(Dataset)
    
    Data = Dataset.data
    Target = Dataset.target

    # 2. manipulate the data
    Data_train,Data_test,Target_train,Target_test = train_test_split(Data, Target, test_size = 0.5)

    # 3. Deside the ML Algoritham
    classifier = DecisionTreeClassifier()
    # Build the data
    classifier.fit(Data_train,Target_train)

    # Tranning the data
    predicitons = classifier.predict(Data_test)

    # Testing the data
    Accuracy = accuracy_score(Target_test,predicitons)

    return Accuracy

def main():
    Ret = MarvellousKNeighbourClassifier()

    print("Accuracy of Iris dataset with DTC is",Ret * 100)
if __name__ == "__main__":
    main()

"""




















"""
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def MarvellousKNeighbourClassifier():
    # 1. Load the data 
    Dataset = load_iris()

    Data = Dataset.data
    Target = Dataset.target

    # 2. manipulate the data
    Data_train,Data_test,Target_train,Target_test = train_test_split(Data, Target, test_size = 0.5)

    # 3. Deside the ML Algoritham
    classifier = DecisionTreeClassifier()
    # Build the data
    classifier.fit(Data_train,Target_train)

    # Tranning the data
    predicitons = classifier.predict(Data_test)

    # Testing the data
    Accuracy = accuracy_score(Target_test,predicitons)

    return Accuracy

def main():
    Ret = MarvellousKNeighbourClassifier()

    print("Accuracy of Iris dataset with DTC is",Ret * 100)
if __name__ == "__main__":
    main()

"""






















"""
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def MarvellousKNeighbourClassifier():
    # 1. Load the data 
    Dataset = load_iris()

    Data = Dataset.data
    Target = Dataset.target

    # 2. manipulate the data
    Data_train,Data_test,Target_train,Target_test = train_test_split(Data, Target, test_size = 0.5)

    # 3. Deside the ML Algoritham
    classifier = KNeighborsClassifier()

    # Build the data
    classifier.fit(Data_train,Target_train)

    # Tranning the data
    predicitons = classifier.predict(Data_test)

    # Testing the data
    Accuracy = accuracy_score(Target_test,predicitons)

    return Accuracy

def main():
    Ret = MarvellousKNeighbourClassifier()

    print("Accuracy of Iris dataset with KNN is",Ret * 100)
if __name__ == "__main__":
    main()

"""



















"""

import numpy as np 
from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()

print("Feature name of iris data set")
print(iris.feature_names)

print("Target names of iris data set")
print(iris.target_names)

# Indicase of remove elements
test_index = [1,51,101]

# Tranning data with remove elements
train_target = np.delete(iris.target, test_index)
train_data = np.delete(iris.data,test_index,axis=0)

# Testing data for testing on tranning data
test_target = iris.target[test_index]   # A B C
test_data = iris.data[test_index]   # 1234  #1234   # 1234

classifier = tree.DecisionTreeClassifier()

classifier.fit(train_data, train_target)

print("Value that we removed for testing")
print(test_target)

"""
























"""

from sklearn.datasets import load_iris

iris = load_iris()

print("Feature name of iris data set")
print(iris.feature_names)

print("Target names of iris data set")
print(iris.target_names)

print("First 10 elements from iris data set")

for i in range(len(iris.target)):
    print("ID : %d, Label %s, Feature : %s" % (i,iris.data[i],iris.target[i]))

"""





















"""

from sklearn import tree

# Load the dataset
# Rough     1
# Smooth    0

# Tennis    1
# Criket    2
def BALL(weigth, surface):
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    #Deside the Machine learning algorithem
    obj = tree.DecisionTreeClassifier()

    # Deside the traning of model
    obj = obj.fit(Features, Labels)

    # Perform the testing 
    ret = (obj.predict([[weigth, surface]]))

    if (ret == 1):
        print("Its Tennis Ball")
    else:
        print("Its, Cricket Ball")

def main():
    print("------------Ball predict case study-----------")

    print("Please enter the weigth in grams ")
    weigth = int(input())

    print("Please enter the surface in (rougth/ smooth)")
    surface = (input())

    if (surface.lower() == "rougth"):
        surface = 1
    elif (surface.lower() == "smooth"):
        surface = 0
    else:
        print("Invalid type of surface")
        exit()

    BALL(weigth, surface)

if __name__ == "__main__":
    main()


"""













"""
from sklearn import tree

# Load the dataset
# Rough     1
# Smooth    0

# Tennis    1
# Criket    2
def BALL():
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    #Deside the Machine learning algorithem
    obj = tree.DecisionTreeClassifier()

    # Deside the traning of model
    obj = obj.fit(Features, Labels)

    # Perform the testing 
    print(obj.predict([[97,0],[35,1]]))

def main():
    BALL()

if __name__ == "__main__":
    main()

"""














"""
import pandas as pd
from sklearn import preprocessing
from sklearn.datasets import load_iris
import numpy as np

def Import_iris():
    iris = load_iris()
    
    data =iris.data
    target = iris.target

    df = pd.DataFrame(data)
    df = pd.DataFrame(target)

    print(df)

    df.to_csv('iris_case_study.csv', index=True)

def main():
    print("------Email sender of iris case study by using Automation script by Swapnil patil------")

    Import_iris()

if __name__ == "__main__":
    main() 

"""

















"""

features_name = ['Alcohol','Malic_acid','Ash','Alcalinity_of_ash','Magnesium','Totalphenols','Flavanoids','Nonflavanoid_phenols','Proanthocyanins','Color_intensity','Hue','OD280/OD315_of_diluted_wines','Proline']
print("Names of features", features_name)
print("--------------------------------------------------------------------------------")

Alcohol = data.Alcohol
Malic_acid = data.Malic_acid
Ash = data.Ash
Alcalinity_of_ash = data.Alcalinity_of_ash
Magnesium = data.Magnesium
Totalphenols = data.Totalphenols
Flavanoids = data.Flavanoids
Nonflavanoid_phenols = data.Nonflavanoid_phenols
Proanthocyanins = data.Proanthocyanins
Color_intensity = data.Color_intensity
Hue = data.Hue
diluted_wines = data.diluted_wines
Proline = data.Proline

le = preprocessing.LabelEncoder()

Alcohol_encoded = le.fit_transform(Alcohol)
print(Alcohol_encoded)
print("-------------------------------------------------------------------------------------")
Malic_acid_encoded = le.fit_transform(Malic_acid)
print(Malic_acid_encoded)
print("-------------------------------------------------------------------------------------")
Ash_encoded = le.fit_transform(Ash)
print(Ash_encoded)
print("-------------------------------------------------------------------------------------")
Alcalinity_of_ash_encoded = le.fit_transform(Alcalinity_of_ash)
print(Alcalinity_of_ash_encoded)
print("-------------------------------------------------------------------------------------")
Magnesium_encoded = le.fit_transform(Magnesium)
print(Magnesium_encoded)
print("-------------------------------------------------------------------------------------")
Totalphenols_encoded = le.fit_transform(Totalphenols)
print(Totalphenols_encoded)
print("-------------------------------------------------------------------------------------")
Flavanoids_encoded = le.fit_transform(Flavanoids)
print(Flavanoids_encoded)
print("-------------------------------------------------------------------------------------")
Nonflavanoid_phenols_encoded = le.fit_transform(Nonflavanoid)
print(Nonflavanoid_phenols_encoded)
print("-------------------------------------------------------------------------------------")
Proanthocyanins_encoded = le.fit_transform(Proanthocyanins)
print(Proanthocyanins_encoded)
print("-------------------------------------------------------------------------------------")
Color_intensity_encoded = le.fit_transform(Color_intensity)
print(Color_intensity_encoded)
print("-------------------------------------------------------------------------------------")
Hue_encoded = le.fit_transform(Hue)
print(Hue_encoded)
print("-------------------------------------------------------------------------------------")
diluted_wines_encoded = le.fit_transform(diluted_wines)
print(diluted_wines_encoded)
print("-------------------------------------------------------------------------------------")
Proline_encoded = le.fit_transform(Proline)
print(Proline_encoded)
print("-------------------------------------------------------------------------------------")

"""








"""
 Code : This Automation script is accept the .xlsx file dataframe and encoding the data and dispay and store 
        the scatterplot daigram using matplotlib. 
        This daigram is send perodiclly using sheduler through the mail. 
"""











"""
import os
import time
import imghdr
import smtplib
import datetime
import schedule
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from email.message import EmailMessage

def Ball_Scatterplot_Casestudy():
    excel_file = 'Ball_into_df.xlsx'
    data = pd.read_excel(excel_file)

    print("Size of actual dataset is :",len(data))

    feature_names = ['Weigth','Features','Labels']

    print("Names of Features", feature_names)
    print("-------------------------------------------------------------")

    weigth = data.Weigth
    features = data.Features
    labels = data.Labels

    le = preprocessing.LabelEncoder()

    weigth_encoded = le.fit_transform(features)
    print(weigth_encoded)
    print("-------------------------------------------------------------")

    features_encoded = le.fit_transform(weigth)
    print(features_encoded)
    print("-------------------------------------------------------------")

    labels_encoded = le.fit_transform(labels)
    print(labels_encoded)
    print("-------------------------------------------------------------")

    plt.scatter(features,weigth, color="b")
    plt.plot(features,weigth, color="r")
    plt.title("Ball_Predictor_CaseStudy")
    plt.xlabel("weigth")
    plt.ylabel("Surface")
    plt.plot(features,weigth, color="r")
    plt.savefig('C:/python/Ball_df_Graph.png', transparent=False, bbox_inches='tight')
    plt.show()

def Email_sending_with_image():
    Sender_Email = 'swapnilpatil46117@gmail.com'
    Reciever_Email = 'devapukale929@gmail.com'
    Password = 'xvfxeadltnyzbfxj' 

    email = EmailMessage()                         
    email['Subject'] = "Using Automation script sending the file." 
    email['From'] = Sender_Email                   
    email['To'] = Reciever_Email                   
    email.set_content('This is a *scatter+plot* image, created by using the matplotlib library.') 

    with open('Ball_df_Graph.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    email.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
        smtp.login(Sender_Email, Password)              
        smtp.send_message(email)

        print("Current time is : ",datetime.datetime.now())

def main():
    print("-------Perodiclly Mail send with file using Automation script by Swapnil Patil--------")

    Ball_Scatterplot_Casestudy()

    Email_sending_with_image()

    schedule.every(1).minutes.do(Email_sending_with_image)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
"""















"""


import os
import imghdr
import smtplib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from email.message import EmailMessage

excel_file = 'Ball_into_df.xlsx'
data = pd.read_excel(excel_file)

print("Size of actual dataset is :",len(data))

feature_names = ['Weigth','Features','Labels']

print("Names of Features", feature_names)
print("-------------------------------------------------------------")

weigth = data.Weigth
features = data.Features
labels = data.Labels

le = preprocessing.LabelEncoder()

weigth_encoded = le.fit_transform(features)
print(weigth_encoded)
print("-------------------------------------------------------------")

features_encoded = le.fit_transform(weigth)
print(features_encoded)
print("-------------------------------------------------------------")

labels_encoded = le.fit_transform(labels)
print(labels_encoded)
print("-------------------------------------------------------------")

plt.scatter(features,weigth, color="b")
plt.plot(features,weigth, color="r")
plt.title("Ball_Predictor_CaseStudy")
plt.xlabel("weigth")
plt.ylabel("Surface")
plt.plot(features,weigth, color="r")
plt.savefig('C:/python/Ball_df_Graph.png', transparent=False, bbox_inches='tight')
plt.show()

Sender_Email = 'swapnilpatil46117@gmail.com'
Reciever_Email = 'devapukale929@gmail.com'
Password = input('Enter your email account password: ')

email = EmailMessage()                         
email['Subject'] = "Using Automation sending the file." 
email['From'] = Sender_Email                   
email['To'] = Reciever_Email                   
email.set_content('This is a *scatter* image, created using the matplotlib library') 

with open('Bappa.png', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name

email.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(email)
"""
















"""
import smtplib
import imghdr
from email.message import EmailMessage

Sender_Email = 'swapnilpatil46117@gmail.com'
Reciever_Email = 'navanathgaikwad7010@gmail.com'
Password = input('Enter your email account password: ')

newMessage = EmailMessage()                         
newMessage['Subject'] = "Check out the new logo" 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content('Let me know what you think. Image attached!') 

with open('Bappa.png', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name

newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)

"""















"""
import smtplib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from email.message import EmailMessage

excel_file = 'Ball_into_df.xlsx'
data = pd.read_excel(excel_file)

print("Size of actual dataset is :",len(data))

feature_names = ['Weigth','Features','Labels']

print("Names of Features", feature_names)
print("-------------------------------------------------------------")

weigth = data.Weigth
features = data.Features
labels = data.Labels

le = preprocessing.LabelEncoder()

weigth_encoded = le.fit_transform(features)
print(weigth_encoded)
print("-------------------------------------------------------------")

features_encoded = le.fit_transform(weigth)
print(features_encoded)
print("-------------------------------------------------------------")

labels_encoded = le.fit_transform(labels)
print(labels_encoded)
print("-------------------------------------------------------------")

plt.scatter(features,weigth, color="b")
plt.plot(features,weigth, color="r")
plt.title("Ball_Predictor_CaseStudy")
plt.xlabel("weigth")
plt.ylabel("Surface")
plt.plot(features,weigth, color="r")
plt.savefig('C:/python/Ball_df_Graph.png', transparent=False, bbox_inches='tight')
plt.show()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('swapnilpatil46117@gmail.com', 'xvfxeadltnyzbfxj')

email = EmailMessage()
email['From'] = 'swapnilpatil46117@gmail.com'
email ['To'] = 'devapukale929@gmail.com'
email['Subject'] = 'C:/python/Ball_df_Graph.png'
email.set_content("Auto mail sender application in python.")
server.send_message(email)

files = ['Ball_df_Graph.png']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    email.add_attachment(file_data, maintype='application', subtype='octet-stream',filename='file_name')


"""





"""
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('swapnilpatil46117@gmail.com', 'xvfxeadltnyzbfxj')
    
    email = EmailMessage()
    email['From'] = 'swapnilpatil46117@gmail.com'
    email ['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {'navnath':'navanathgaikwad7010@gmail.com', 'deva':'devapukale929@gmail.com'}

def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()

    send_email(receiver, subject, message)

def main():
    get_email_info()

if __name__ == "__main__":
    main()
"""








"""
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('swapnilpatil46117@gmail.com', 'xvfxeadltnyzbfxj')
server.sendmail('swapnilpatil46117@gmail.com', 'navanathgaikwad7010@gmail.com', 'Mail send from python, hii noni')

"""


"""
# Mail sender Attempt 1

import smtplib

server =smtplib.SMTP('smtp.gamil.com',587)

server.starttls()

server.login('swapnilpatil46117@gmail.com', 'xvfxeadltnyzbfxj')

server.sendmail('swapnilpatil46117@gmail.com', 'devapukale929@gmail.com', 'Mail send from python')

print('Mail send')
"""






"""

# Mail sender Attempt 2

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'swapnilpatil46117@gmail.com'
email_password = 'tksfyjlvrpedvniu'

email_receiver = 'devapukale929@gmail.com'

subject = "Mail send by python application"
body = """
 #Ram krushn hari, Mauli
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gamil.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
"""









"""
mail password : xvfxeadltnyzbfxj

mail password : tksfyjlvrpedvniu
"""


 
"""
import smtplib

#smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]])
 
sender = 'swapnilpatil46117@gmail.com'
receivers = 'kashilingpukale@gmail.com'

message = "hii i am swapnil"

try:
    smtpObj = smtplib.SMTP('localhost')
    smtplib.sendmail(sender, receivers, message)
    print("Successsfully send mail")
except Exception:
    print("Error : unable to send mail")
"""










"""
import pandas as pd
from sklearn import preprocessing

excel_file = 'Ball_into_df.xlsx'
data = pd.read_excel(excel_file)

print("Size of actual dataset is :",len(data))

feature_names = ['Weigth','Features','Labels']

print("Names of Features", feature_names)
print("-------------------------------------------------------------")

weigth = data.Weigth
features = data.Features
labels = data.Labels

le = preprocessing.LabelEncoder()

weigth_encoded = le.fit_transform(features)
print(weigth_encoded)
print("-------------------------------------------------------------")

features_encoded = le.fit_transform(weigth)
print(features_encoded)
print("-------------------------------------------------------------")

labels_encoded = le.fit_transform(labels)
print(labels_encoded)
print("-------------------------------------------------------------")
"""











"""
# import required library
import pandas as pd
from sklearn import preprocessing

# Dataframe weigth, feature, label columns
Weigth = [35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,]
Features = ["Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth"]
Labels = ["Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket"]

# Create labelEncoder
le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
Weigth_encoder = le.fit_transform(Weigth)
print(Weigth_encoder)
print("-------------------------------------------------------------------------")

# Converting string labels into numbers.
Features_encoder = le.fit_transform(Features)
print(Features_encoder)
print("-------------------------------------------------------------------------")

# Converting string labels into numbers.
Labels_encoder = le.fit_transform(Labels)
print(Labels_encoder)
print("-------------------------------------------------------------------------")

"""





"""
# import required library
import pandas as pd
from sklearn import preprocessing

# Load dataset

data = pd.read_excel('Ball_into_df.xlsx', sheet_name = 0, index_col=0)

print("size of Actual dataset : ",len(data))

feature_names = ['Weigth', 'Features', 'Labels']
print("Name of Features", feature_names)

weigth = data.Weigth
feature = data.Features
labels = data.Labels

# Create labelEncoder
le = preprocessing.LabelEncoder()
   
# Converting string labels into numbers.
Weigth_encoder = le.fit_transform(weigth)
print(Weigth_encoder)
print("-------------------------------------------------------------------------")

# Converting string labels into numbers.
Features_encoder = le.fit_transform(feature)
print(Features_encoder)
print("-------------------------------------------------------------------------")

# Converting string labels into numbers.
Labels_encoder = le.fit_transform(labels)
print(Labels_encoder)
print("-------------------------------------------------------------------------")


"""










"""
# import required library
import pandas as pd
from sklearn import preprocessing

# Dataframe weigth, feature, label columns
Weigth = [35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,]
Features = ["Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth"]
Labels = ["Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket"]

# Create labelEncoder
le = preprocessing.LabelEncoder()
   
# Converting string labels into numbers.
Weigth_encoder = le.fit_transform(Weigth)
print(Weigth_encoder)
print("-------------------------------------------------------------------------")

# Converting string labels into numbers.
Features_encoder = le.fit_transform(Features)
print(Features_encoder)
print("-------------------------------------------------------------------------")

# Converting string labels into numbers.
Labels_encoder = le.fit_transform(Labels)
print(Labels_encoder)
print("-------------------------------------------------------------------------")
"""











"""
import pandas as pd
#from xlsxwriter import Workbook

df = pd.DataFrame({'Data' : [11,21,51,101,111,121],'Labels' : [111,221,251,1021,1211,1221]})

writer = pd.ExcelWriter('MarvellousPandas.xlsx')

df.to_excel(writer, sheet_name='Sheet1')

writer.save()
"""












"""

import pandas as pd

df = pd.DataFrame({'student' : ["sp","gp"], 'labels' : [11,22]})
writer = pd.ExcelWriter('sp.xlsx')
df.to_excel(writer, sheet_name='sheet1')
writer.save()

"""    




















"""

import pandas as pd 

# print("Dataframe with list")
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)
print("----------------------")

# print("Dataframe with list")
data = [['PPA',4],['LB',3],['Python',3],['Anguler',3]]
df = pd.DataFrame(data, columns=['Name','Duration'])
print(df)
print("-----------------------")

data = {'Name' : ['PPA', 'LB', 'Python', 'Anguler', 'LSP'], 'Duratioon' : [4,3,3,3,5]}
df = pd.DataFrame(data)
print(df)
print("-----------------------")

data = [{'Name':'PPA','Duration':3,'Fees':10500},{'Name':'LB','Duration':4,'Fees':18000},{'Name':'Python','Duration':5,'Fees':18500}]
df = pd.DataFrame(data)
print(df)


"""















"""
import pandas as pd
import numpy as np

data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s[0])
print("----------------------------------")

# Costomize indexing 
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,200,300,400])
print(s[300])
print("----------------------------------")

data = {'a' : 0.1, 'b' : 0.2, 'c' : 0.3}
s = pd.Series(data)
print(s)
print("----------------------------------")

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s['c'])


"""




"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():

    # Load data
    X = [8,12,15,5,7,2,3,12,9,4]
    Y = [8,10,3,4,7,6,5,10,4,9]

    print("Values of Independent variables x",X)
    print("Values of Dependent variables y",Y)

    # Least Square method
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("Mean of Independent variable x",mean_x)
    print("Mean of Dependent variable y",mean_y)
    n = len(X)

    numerator = 0
    denomenator = 0

    # Equation of line is : y = mx + c

    for i in range(n):
        numerator += (X[i] - mean_x)*(Y[i] - mean_y)

        denomenator += (X[i] - mean_x)**2

    m = numerator / denomenator

    # c = y' -mx'

    c = mean_y - (m * mean_x)

    print("Slope of Regression line is : ",m)       
    print("Y Intercept of Regression line is",c)    

    # Display plotting of above points
    x = np.linspace(1,6,n)

    y = c + m * x

    plt.plot(x,y, color='r', label='Regression Line')

    plt.scatter(X,Y, color='b' ,label='scatter plot')

    plt.xlabel('X - Independent Variable')
    plt.ylabel('Y - Dependent Variable')

    plt.legend()
    plt.show()

    # Findout goodness of fit is R Square
    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m * X[i]
        ss_t += (Y[i] - mean_y)**2
        ss_r += (Y[i] - y_pred)**2

    r2 = 1 - (ss_r/ss_t)    

    print("Goodness of fit using R2 method is",r2)

def main():
    print("----------HeadBrain CaseStudy by Swapnil Patil----------")

    print("--------------Supervised Machine Learning---------------")

    print("----Linear Regreesion----")

    MarvellousPredictor()

if __name__ == "__main__":
    main()

"""











"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def HeadBrainPredictor():

    # Load data
    data = pd.read_csv("HeadBrain.csv")

    print("Size of data set",data.shape)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    # Least Square method
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("Mean of Independent variable x",mean_x)
    print("Mean of Dependent variable y",mean_y)
    n = len(X)

    numerator = 0
    denomenator = 0

    # Equation of line is : y = mx + c

    for i in range(n):
        numerator += (X[i] - mean_x)*(Y[i] - mean_y)

        denomenator += (X[i] - mean_x)**2

    m = numerator / denomenator

    # c = y' -mx'

    c = mean_y - (m * mean_x)

    print("Slope of Regression line is : ",m)       
    print("Y Intercept of Regression line is",c)   

    max_x = np.max(X)+100
    min_x = np.min(X)-100

    # Display plotting of above points
    x = np.linspace(min_x,max_x,n)

    y = c + m * x

    plt.plot(x,y, color='#58b970', label='Regression Line')

    plt.scatter(X,Y, color='#ef5423' ,label='scatter plot')

    plt.xlabel('Head size in cm3')
    plt.ylabel('Brain size in grams')

    plt.legend()
    plt.show()

    # Findout goodness of fit is R Square
    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m * X[i]
        ss_t += (Y[i] - mean_y)**2
        ss_r += (Y[i] - y_pred)**2

    r2 = 1 - (ss_r/ss_t)    

    print("Goodness of fit using R2 method is",r2)

def main():
    print("----------HeadBrain CaseStudy by Swapnil Patil----------")

    print("--------------Supervised Machine Learning---------------")

    print("----Linear Regreesion on Head and Brain size data set---")
    print("--------------------------------------------------------")

    HeadBrainPredictor()

if __name__ == "__main__":
    main()

"""








"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def HeadBrainPredictor():

    # Load data
    data = pd.read_csv("HeadBrain.csv")

    print("Sixe of data set is :",data.shape)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    X = X.reshape((-1,1))

    n = len(X)

    reg = LinearRegression()

    reg = reg.fit(X,Y)

    y_pred = reg.predict(X)

    r2 = reg.score(X,Y)

    print(r2)

def main():
    print("----------HeadBrain CaseStudy by Swapnil Patil----------")

    print("Supervised Machine Learning")

    print("Linear Regreesion on Hrad and Brain size data set")

    HeadBrainPredictor()

if __name__ == "__main__":
    main()

"""
















"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def MarvellousHeadBrainPredictor():

    # Load Data
    data = pd.read_csv('headbrain.csv')

    print("Size if data set",data.shape)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    X = X.reshape((-1,1))

    n = len(X)

    reg = LinearRegression()

    reg = reg.fit(X,Y)

    y_pred = reg.predict(X)

    print(y_pred)

    r2 = reg.score(X,Y)

    print(r2)   

def main():
    print("-----------HeadBrain case study by swapnil patil------------")

    print("Supervised Machine Learning")

    print("Linear Regreesion")

    MarvellousHeadBrainPredictor()

if __name__ == "__main__":
    main()


"""





















"""
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def CaseStudy(DataSet):
    # Step 1 : Load the dataset
    Data = pd.read_csv(DataSet, index_col = 0)
    print("Dataset is  : ",len(Data))

    # Step 2 : Clenning ,prepere, manipulate the datset
    features_name = ['Whether','Temperature']
    print(features_name)

    Whether = Data.Whether
    Temperature = Data.Temperature
    play = Data.Play

    # Creting the label incoded
    le = preprocessing.LabelEncoder()

    # Converting string into numbres
    whether_encoder = le.fit_transform(Whether)
    print(whether_encoder)

    # Converting string into numbres
    temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(play)

    print(temp_encoded)

    # combining the whether and temprature in a single list of tuple
    features = list(zip(whether_encoder,temp_encoded))

    # Step : 3 Traing data
    model = KNeighborsClassifier(n_neighbors = 3)

    # train the model using a traning datset
    model.fit(features,label)

    first = int(input("Enter the whether in number : (1:Rainy, 2:Sunny, 3:Overcast)\n"))
    Secound = int(input("Enter the temprature number : (0:Cool, 1:Hot, 3:Mild)\n"))

    # Step 4 : Test data
    predict = model.predict([[first,Secound]]) 
    if predict == 1:
        print("Now you can play.")
    else:
        print("Don't play.")
       
def main():
    print("-----------Case study by swapnil patil------------")

    CaseStudy("PlayPredictor.csv")

if __name__ == "__main__":
    main()

"""




















"""

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):

    # Step 1 : Load Data
    data = pd.read_csv(data_path, index_col=0)

    print(data.head(2)) 

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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

def Marvellous():
    # 1 Load the data
    Dataset = pd.read_csv('PlayPredictor.csv',usecols = ['Whether','Temperature','Play'])
    print(Dataset)

    print("--------------------")
    Dataset.head()
    print("========================================")
    Dataset.info()

    Data = Dataset.Data
    Target = Dataset.target

    # 2 Manipulate the data
    Data_train, Data_test, Target_train, Target_test = train_test_split(Data, Target, test_size = 0.5)

    Classifier = KNeighborsClassifier()

    Classifier.fit(Data_train,Target_train)

    Predictions = Classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test, Predictions)

    return Accuracy

def main():

    Ret = Marvellous()

    print("Accuracy of Dataset with KNN is : ",Ret)

if __name__ == "__main__":
    main()

"""

































"""
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













"""
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from scipy.spatial import distance
from sklearn import tree

def MarvellousTree():
    iris = load_iris()

    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.5)

    classifier = tree.DecisionTreeClassifier()

    classifier.fit(data_train, target_train)

    Predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, Predictions)

    return Accuracy

def MarvellousKNN():
    iris = load_iris()

    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.5)

    classifier = KNeighborsClassifier()

    classifier.fit(data_train, target_train)

    Predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, Predictions)

    return Accuracy

def main():
    Accuracy = MarvellousTree()
    print("Tree : ",Accuracy*100,"%")

    Accuracy = MarvellousKNN()
    print("KNN : ",Accuracy*100,"%")

if __name__ == "__main__":
    main()

"""

"""










"""

"""
# user defined Module using

from sklearn.datasets import load_iris
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
    Dataset = load_iris()       # 1 Load the data

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

"""

























"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder 
from sklearn.model_selection import train_test_split
import seaborn as sns


# Loading dataset
wine = pd.read_csv('winequality-red.csv',sep=';')

wine.head()
wine.info()
wine.isnull().sum()

#prprocessing data
bins = (2,6.5,8)
group_names = ['bad','good']
wine['quality'] = pd.cut(wine['quality'], bins = bins, labels = group_names)
wine['quality'].unique()

label_quality = LabelEncoder()

wine['quality'] = label_quality.fit_transform(wine['quality'])
wine.head()
wine['quality'].value_counts()
sns.countplot(wine['quality'])



X = wine.drop('quality', axis = 1)
y = wine['quality']

# train and test the data
X_train, X_test, y_test, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_train = sc.transeform(X_train)
X_test = sc.transeform(X_test)

X_train[]

"""





"""
students = ["ram","shyam","kishan","radha","radhika"]

for student in students:
    if student == "kishan":
        continue;
    print(student)

"""

"""
marks = (95,97,98,97,97)
print(marks.count(97))
print(marks.index(97))
"""

"""
marks = {95,97,98,97,97}
print(marks)
"""


"""
marks = {"Engish" : 95, "Chrmistry" : 97, "Physics" : 98, "Computer" : 97,"maths" : 97}
print(marks["Computer"])
marks["Physics"] = 99
print(marks)
"""

"""
from math import sqrt

print(sqrt(16))
"""


"""
def print_sum(first,secound = 4):
    print(first + secound)

print_sum(1)

"""






"""
mark = [98,34,65,"math"]
print(mark[0:3])

for score in mark:
    print(score)

mark.append(99)
print(mark)    
mark.insert(0,9)
print(99 in mark)    
print(91 in mark) 
print(len(mark))
print("-----------------")
mark = [98,34,65,"math"]

i = 0

while i < len(mark):
    print(mark[i])
    i = i + 1

mark.clear()
print(mark)


"""











"""
# Calculater

first = int(input("Enter first number : "))
operator = input("enter operator (+,-,*,/,%) : ")
secound = int(input("Enter secound number : "))

if operator == "+":
    print(first + secound)
elif operator == "-":
    print(first - secound)
elif operator == "*":
    print(first * secound)
elif operator == "/":
    print(first / secound)
elif operator == "%":
    print(first % secound)
else:
    print("Invalid opration")
"""




"""
name = "Sapnil Patil"
print(name.replace("patil", "Ironman"))
name = "Sapnil Patil"
print("P" in name)
name = "Sapnil Patil"
print("-----------------")
print(3 < 2)
print(3 > 2)
print(3 == 3)
print(3 == 2)
print(3 != 3)
print("----------------")
print(2 > 3 or 2 > 1)
print(3 >2 and 2 > 3)
print("-------------------------")
age = 1
if age >= 18:
    print("You are in adult")
    print("You can vote")
elif age < 18 and age > 3:
    print("You are a student")
else:
    print("You are a child")


"""







"""
# import requried libarary
from sklearn import tree
from sklearn import metrics

# Load the dataset
# Rough     1
# Smooth    0

# Tennis    1
# Criket    2

def BallPredictor():
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    #Deside the Machine learning algorithem
    obj = tree.DecisionTreeClassifier()

    # Perform the treanning of model
    obj = obj.fit(Features, Labels)

    # perform of testing 
    print(obj.predict([[97,0]]))

    print(metrics.confusion_matrix(Labels,[[97,0]]))

def main():
    print("-------------Ball Predictor Case Study------------")

    BallPredictor()

if __name__ == "__main__":
    main()

"""















"""
import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'swapnilpatil46117@gmail.com'
email_password = os.environ.get("EMAIL_PASSWORD")
email_receiver = 'kashilingpukale@gmail.com'

subject = "Automation mail sender by using python."
body = """
"""

em = EmailMessage[]
em['From'] = email_sender
em['To'] = email_receiver
em[subject] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

"""




















"""
import smtplib

sender = "from@swapnilpatil46117@gmail.com"
receivers = ["gvaibhav1002@gmail.com"]
"""
""" : Automation using python application
To = To Person
Subject : SMTP email test
This is a test e-mail message.
"""
"""
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("Successsfully send email")
except Exception:
    print("Error : Unable to send email.")
"""





















"""
from sys import*
import os
import hashlib

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DirectoryChecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')

        NewName = "Log1.txt"
        fd = open(NewName,"a")
        fd.write(file_hash)
        
    else:
        print("Invalid Path")

def main():
    print("-------Application of checksum files---------")

    print("Application name : "+argv[0])

    if(len(argv) != 2):
        print("Invalid argument..")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : Accept directory and display checksum of all files.")

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_Name directory_Name")

    DirectoryChecksum(argv[1])

if __name__ == "__main__":
    main()


"""














"""
        ----------------------Supervised Machine Learning-----------------------------
            --------User Defined K Nearest Neighbour Algoritham-----------
    ----------------------------------------------------------------------------------------
    * In this application we create our own algoritham for classified machine learning.
    * We create our own K Nearest Neighbour algoritham.
    * For user defined algoritham we design one class named as MarvellousKNN.
    * This class contains 3 methoads as fit, predict, closest method.
    * There is one naked method euc() which calculate distance between two points using 
        Eucclidean distance algorithm.
    * fit() method initialise traning data and its targets iniside class.
    * predict() method creates one array as prediction which store stortest distance between
        all test data and traning data elements.
    * predict() method calls closest methoad ehich returns tyhe shortest distance.
  ---------------------------------------------------------------------------------------------
 - Consider below characteristics of Machine Learning Application :
        
        Classifire :         User defined K Nearest Neighbour
        DataSet :            Iris Dataset
        Features :           Sepal Width, Sepal Length, Petal Width, Petal Length
        Labels :             Versicolor, Sentosa, Virginica
        Tranning Dataset :      75 Entries
        Testing Dataset :       75 Entries
"""
"""
from sklearn import tree
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a,b):
    return distance.euclidean(a,b)

class MarvellousKNN():
    def fit(self,TranningData,TranningTarget):
        self.TranningData = TranningData
        self.TranningTarget = TranningTarget

    def predict(self,TestData):
        predictions = []
        for row in TestData:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self, row):
        bestdistance = euc(row, self.TranningData[0])
        bestindex = 0
        for i in range(1,len(self.TranningData)):
            dist = euc(row,self.TranningData[i])
            if dist < bestdistance:
                bestdistance = dist
                bestindex = i   
        return self.TranningTarget[bestindex]

def MarvellousKNeighbor():
    border = "-"*50

    iris = load_iris()

    data = iris.data
    target = iris.target

    print(border)
    print("Actual data set")
    print(border)

    for i in range(len(iris.target)):
        print("ID : %d,Label %s, Feature : %s"%(i,iris.data[i],iris.target[i]))
    print("Size of Actual data set %d"%(i+1))

    data_train, data_test, target_train, target_test = train_test_split(data,target, test_size = 0.5)

    print(border)
    print("Tranning data set")
    print(border)

    for i in range(len(data_train)):
        print("ID : %d,Label %s,Feature : %s"%(i,data_train[i],target_train[i]))
    print("Size of Traning data set %d"%(i+1))

    print(border)
    print("Test data set")
    print(border)

    for i in range(len(data_test)):
        print("ID : %d,Label %s, Feature : %s"%(i,data_test[i],target_test[i]))
    print("Size of Test data set %d"%(i+1))
    print(border)

    classifier = MarvellousKNN()

    classifier.fit(data_train,target_train)

    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, predictions)

    return Accuracy

def main():

    Accuracy = MarvellousKNeighbor()
    print("Accuracy of classification algoritham with K Neighbor classifier is",Accuracy*100,"%")

if __name__ == "__main__":
    main()
"""



















"""

    -------------------Supervised Machine Learning----------------------------
        ----Accuracy Calculation with Decision Tree & K Nearest Neighbour-----
    * In this application we train iris data set with Decision Tree algorithem and K Nearest Neighbour algorithm.
    * We divide iris data set into two equal part as tranning data and test data.
    * We applay tranning on tranning data and predict the result on test data.
    * We calculate accuracy of both the algorithems by applaying of test data.

    - Consider below characteristics of Machine Learning Application:
        Classifire :    Decision Tree & K Nearest Neighbour
        DataSet :       Iris Dataset
        Features :      Sepal Width, Sepal Length, Petal Width, Petal Length
        Labels :        Versicolor, Sentosa, Virginica
        Tranning Dataset :      75 Entries
        Testing Dataset :       75 Entries
"""
"""
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def MarvellousCalculateAccuracyDecisionTree():
    iris = load_iris()

    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.5)

    classifier = tree.DecisionTreeClassifier()

    classifier.fit(data_train,target_train)

    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, predictions)

    return Accuracy

def MarvellousCalculateAccuracyKNeighbour():
    iris = load_iris()

    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.5)

    classifier = KNeighborsClassifier()

    classifier.fit(data_train, target_train)

    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, predictions)

    return Accuracy

def main():
    Accuracy = MarvellousCalculateAccuracyDecisionTree()
    print("Tree",Accuracy*100,"%")

    Accuracy = MarvellousCalculateAccuracyKNeighbour()
    print("KNN",Accuracy*100,"%")


if __name__ == "__main__":
    main()

"""



















"""

from sklearn import tree

def BallPredictior(weigth, surface):	

	# load the Dataset
		# Rough = 1
		# smooth = 0

		# Tennis = 1
		# Cricket = 2 

	Features = [[35,"1"],[47,"1"],[90,"0"],[48,"1"],[90,"0"],[35,"1"],[92,"0"],[35,"1"],[35,"1"],[35,"1"],[96,"0"],[43,"1"],[110,"0"],[35,"1"],[95,"0"]]

	Labels = ["1","1","2","1","2","1","2","1","1","1","2","1","2","1","2"]

	# Decision the Machine Learning algorithem
	obj = tree.DecisionTreeClassifier()

	# Perform traning of model
	obj = obj.fit(Features, Labels)

	# perform the testing 
	ret = obj.predict([[weigth, subfolder]])
	if ret == 1:
		print("Tennis Ball")
	else:
		print("Cricket Ball") 

def main():
	print("-------------Ball Prediction Case study---------------")

	print("Plese enter the weigth of grams")
	weigth = int(input())

	print("Please surface (Rough/ Smooth)")
	surface = input()

	if surface.lower() == "Rough":
		surface = 1
	elif surface.lower() == "smooth":
		surface = 0
	else:
		print("Invalid type of surface")
		exit()

	BallPredictior(weigth, surface)

if __name__ == "__main__":
	main()

"""




















"""
from sys import*
import os
import hashlib
import time

def DeleteFiles(dict1):
    results = list(filter(lambda x : len(x) > 1,dict1.values()))
    
    icnt=0
    
    if len(results) > 0:
        for result in results:
        	for subresult in result:
	            icnt+=1
	            if icnt >= 2:
	            	os.remove(subresult)
			icnt=0
    else:
        print("No duplicate files found.")

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    
    return hasher.hexdigest()

def findDup(path):
    flag = os.path.isabs(path)
    
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    dups = {}
    
    if exists:
        for foldername, subfolder, fileList in os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
                    
        return dups
    else:
        print("Invalid Path")

def printResults(dict1):
    results = list(filter(lambda x : len(x) > 1,dict1.values()))
    
    if len(results) > 0:
        print("Duplicates Found:")
        print("The following file are duplicate")
        for result in results:
            for subresult in result:
                print("\t\t%s"% subresult)
    else:
        print("No duplicate files found.")

def main():
    print("-----Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        arr = {}
        startTime = time.time()
        arr = findDup(argv[1])
        printResults(arr)
        DeleteFiles(arr)
        endTime = time.time
        
        print("Took %s secound to evaluate." % (endTime - startTime))

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()
"""





















"""

from itertools import count
from platform import python_branch
from turtle import pu
import pyautogui
import time

time.sleep(4)
count=0
while count <= 5 :
    pyautogui.typewrite("Hello")
    pyautogui.press("enter")
    count=count+1

"""



"""
import sys
import os
import psutil
import socket
import platform
import time
import datetime
import wmi


#This is Platform Analyser Which Shows Our Platform Specification 

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    return "%d:%02d" % (hour, minutes)

def main():

    Date= str(datetime.date.today())
    Time_t1 = time.localtime()
    current_time = str(time.strftime("%H-%M-%S",Time_t1))

    current_time1 = str(time.strftime("%H:%M:%S",Time_t1))
    filename=str(str(current_time)+str(Date)) 
    File1= open( str(filename +".txt"),"w")

    Device_Name =str(socket.gethostname())
    Machine_Type = str(platform.machine())
    Processor_Name =str(platform.processor())
    Platform_Type =str(platform.platform())
    OS_Name=str(platform.system())
    Architecture= str(platform.architecture())
    OS_Version =str(platform.version())    

    Total_Ram=str(((psutil.virtual_memory().total)/1000000000))
    Used_Ram=str(((psutil.virtual_memory().used)/1000000000))
    Available_Ram=str(((psutil.virtual_memory().available)/1000000000))    

    User_name =str(os.getlogin())

    Total_Cores = str( psutil.cpu_count())
    Logical_Cores=str(psutil.cpu_count(logical=True))
    Physical_Cores=str(psutil.cpu_count(logical=False))

    battery = psutil.sensors_battery()


    print("-----------------WelCome to System Analyser By Swapnil Patil-----------------\n")
    File1.write("-----------WelCome to System Analyser By Swapnil Patil-----------\n")
    File1.write("-----------------------------------------------------------------------------\n")
    File1.write("Current Date of Creating File:                            "+ Date + "\n")
    File1.write("Current Time of Creating File:                            "+ current_time1 +"\n")
    File1.write("-----------------------------------------------------------------------------\n")
    File1.write("Device  Related Information \n")
    File1.write("Device Name:                                             "+  Device_Name+"\n")
    File1.write("User Name:                                               "+User_name+"\n")    
    File1.write("Architecture:                                            "+Architecture+"\n")
    File1.write("-----------------------------------------------------------------------------\n")
    File1.write("Processor Related Information \n")
    File1.write("Machine Type:                                            "+Machine_Type+"\n")
    File1.write("processor Name:                                          "+ Processor_Name+"\n")
    File1.write("Platform Type:                                           "+ Platform_Type+"\n")
    File1.write("Operating system Name:                                   "+OS_Name+"\n")
    File1.write("Operating System Version:                                "+ OS_Version+"\n")
    File1.write("-----------------------------------------------------------------------------\n")
    File1.write("Cores Related Information \n")
    File1.write("Total Number of Cores:                                   "+Total_Cores +"\n")
    File1.write("Total Number of Logical Cores:                           "+Logical_Cores +"\n")
    File1.write("Total Number of Physical Cores:                          "+Physical_Cores +"\n")
    File1.write("-----------------------------------------------------------------------------\n")
    File1.write("Ram Related Information \n")
    File1.write("Total Size of Ram:                                       "+Total_Ram + "GB\n")
    File1.write("Used  Ram:                                               "+ Used_Ram + "GB\n")
    File1.write("Available Ram:                                           "+ Available_Ram+ "GB\n")
    File1.write("-----------------------------------------------------------------------------\n")
    File1.write("Battery Related Information \n")    
    File1.write("Battery percentage :                                     " + str(battery.percent) +"\n")
    File1.write("Power plugged in :                                       " + str(battery.power_plugged)+"\n")
    File1.write("Battery left(Hours:Minutes) :                            " + str(convert(battery.secsleft))+"\n")

    File1.write("-----------------------------------------------------------------------------\n")

    print("-------------------------------------------------------------------------------")
    print("----------------Your PlatForm Details Are Successsfully Analyzed---------------")
    print("-------------------------------------------------------------------------------")
    print("-----------------Thank you For Using PlatForm Analyzer-------------------------")
    File1.write("------------------Thank you For Using PlatForm Analyzer------------------\n")
    File1.write("------------------------PPA AANI  LB CHI PUNYAYI-------------------------\n") 


if __name__ == "__main__":
    main()

"""



















"""
from sys import*
import os
import hashlib

def hashfile(path, blocksize = 1024):
	afile = open(path, 'rb')
	hasher = hashlib.md5()
	buf = afile.read(blocksize)

	while len(buf) > 0:
		hasher.update(buf)
		buf = afile.read(blocksize)

	afile.close()

	return hasher.hexdigest()

def FindDuplicate(path):
	flag = os.path.abspath(path)

	if flag == False:
		path = os.path.isdir(path)

	exists = os.path.isdir(path)

	dups = {}

	if exists:
		for dirName, subdirs, fileList in os.walk(path):
			for filen in fileList:
				path = os.path.join(dirName, filen)
				file_hash = hashfile(path)
				if file_hash in dups:
					dups[file_hash].append(path)
				else:
					dups[file_hash] = [path]

		return dups
	else:
		print("Invalid Path")

def PrintDuplicate(dict1):
	results = list(filter(lambda x : len(x) > 1, dict1.values()))

	if len(results) > 0:
		print("Duplicate Found : ")

		print("The following files are identical.")

		icnt = 0;
		for result in results:
			for subresult in result:
				icnt+=1
				if icnt >= 2:
					print('\t\t%s' % subresult)

	else:
		print("No duplicate file found.")

def main():
	print("-------Application of Search Duplicate files by Swapnil Patil---------")

	print("Application name : "+argv[0])

	if(len(argv) != 2):
		print("Invalid argument..")
		exit()

	if(argv[1] == "-h") or (argv[1] == "-H"):
		print("Help : Accept directory and display checksum of all files.")
		exit()

	if(argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage : Application_Name directory_Name")
		exit()

	try:
		arr = {}
		arr = FindDuplicate(argv[1])
		PrintDuplicate(arr)

	except ValueError:
		print("Error : Invalid datatype of input")

	except Exception as E:
		print("Error : Invalid input",E)

if __name__ == "__main__":
	main()


"""
















"""
import fnmatch
from sys import*
import os

def DirectoryWatcher(path, extention):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    if exists:
        for foldername, subfolder, filname in os.walk(path):
            for filen in filname:
                if filen.lower().endswith(extention):
                    print(filen)
    else:
        print("Invalid Path")

def main():
    print("-----Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " +argv[0])

    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        DirectoryWatcher(argv[1],argv[2])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()



"""







"""
from sys import*
import os

def DirectoryWatcher(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    if exists:
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : "+foldername)
            for subf in subfolder:
                print("Sub folder of "+foldername+"is :"+subf)
            for filen in filname:
                print("File inside "+foldername+"is : "+filen)
                print("with size : ",os.path.getsize(os.path.join(foldername, filen)))

            print(' ')
    else:
        print("Invalid Path")

def main():
    print("-----Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()
"""



"""
from sys import*
import os

def Directory_Watcher(Dir_Name):
	print("Inside directory watcher methoad")
	print("Name of input directory : ",Dir_Name)



	for Foldername, SubFoldername, Filename in os.walk(Dir_Name):
		print("Folder name : "+Foldername)

		for sub in SubFoldername:
			print("Subfolder name is : "+Foldername+" is "+sub)

		for fname in Filename:
			print("file name is : "+Foldername+" is "+fname+" having size ",os.path.getcwd(fname))

			
			
		print(" ")

	print("Enter the file name that you want to create")
	Name = input()
	
	fd.write(fname)
		
def main():
    print("-----Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " +argv[0])

    if (len(argv) < 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    Directory_Watcher(argv[1])

if __name__ == "__main__":
    main()
"""




"""
import os

def Read_File(FileName):
	if(os.path.exists(FileName)):
		fd = open(FileName, "rb")
		Data = fd.read()
		print("Data from the file is ")
		print(Data)

		fd.close()

	else:
		print("File is not existing")
		return 

def main():
	print("Enter the file name to read")
	Name = input()

	Read_File(Name)

if __name__ == "__main__":
	main()


"""





"""
import os

def Create1(FileName):
	if(os.path.exists(FileName)):
		size = os.path.getsize(FileName)
		if(size == 0):
			os.remove(FileName)
		else:
			print("Are you sure to delete the file")
			option = input()
			if(option == "Y") or (option == "y"):
				os.remove(FileName)
			else:
				print("File deletion process stoped")			
	else:
		print("There is no such file")
		

def main():
	print("Enter the file name ot create")
	Name = input()

	Create1(Name)

if __name__ == "__main__":
	main()
"""


"""
# ProcessMoniter.py

import psutil

def ProcessDisplay():
	listprocess = []

	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs = ['pid', 'name', 'username'])

			listprocess.append(pinfo);

		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass

	return listprocess

def main():
	print("Marvellous Infosystem : ML and AI")

	print("Process Monitor")

	listprocess = ProcessDisplay()

	for elem in listprocess:
		print(elem)

if __name__ == "__main__":
	main()

"""




"""
# AutomationTemplate.py

from sys import *
from os import*

def Script_Task(No):
	if((No % 2) == 0):
		print("It is even number")
	else:
		print("It is odd number")

def main():
	print("---------Marvellous Infosystems Automation-----------")

	print("Automation script started with name : "+argv[0])

	if(len(argv) != 2):
		print("Error : Insufficent argument")
		print("Use -h for help and us -u for usage of the script")
		exit()

	if((argv[1] == "-h") or (argv[1] == "-H")):
		print("Help : This script is used to perform___________")
		exit()

	elif((argv[1] == "-u") or (argv[1] == "-U")):
		print("Usage : provide ____ number of argument as")
		print("First Argument as : _______")
		print("Secound Argument as : _______")
		exit()

	Script_Task(int(argv[1]))

if __name__ == "__main__":
	main()

"""






"""
# Task3.py

import time
import schedule
import datetime


def Task_Hour():
	print("Inside Hour",datetime.datetime.now())

def Task_Day():
	print("Inside Day",datetime.datetime.now())

def fun():
	print("Inside fun",datetime.datetime.now())

def main():
	print("Inside task schedular")
	print("Current time is : ",datetime.datetime.now())

	schedule.every(1).minutes.do(fun)
	schedule.every(1).hour.do(Task_Hour)
	schedule.every().monday.at("17:35").do(Task_Day)

	while(True):
		schedule.run_pending()
		time.sleep(1)

if __name__ == "__main__":
	main()


"""


















"""

import time
import schedule
import datetime
from sys import*
Cnt = 0

def fun():
	print("Inside fun : ",datetime.datetime.now())

def main():
	print("Inside task schedular")
	print("Current time is : ",datetime.datetime.now())

	schedule.every(1).minutes.do(fun)
	global Cnt
	Cnt = Cnt + 1

	if (Cnt == 5):
		sys.exit()

	while(True):
		schedule.run_pending()
		time.sleep(1)

if __name__ == "__main__":
	main()

"""

"""
import time
import schedule
import datetime
from sys import*
import os

No = 0

def fun():
	print("Inside fun : ",datetime.datetime.now())

def scriptTerminater():
	schedule.every().tuesday.at("12:55").do(fun)
 	if (No == 5):
		sys.exit()

def main():
	print("Inside task schedular")
	print("Current time is : ",datetime.datetime.now())

	schedule.every(1).minutes.do(scriptTerminater)

	while(True):
		schedule.run_pending()
		time.sleep(1)

if __name__ == "__main__":
	main()



"""




"""
import time
import schedule
import datetime

def fun():
	print("Inside fun")

def main():
	print("Inside task schedular")

	schedule.every(1).minutes.do(fun)

	while(True):
		schedule.run_pending()
		time.sleep(1)

if __name__ == "__main__":
	main()

"""









"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
"""


"""
import requests
import re
from urllib.parse import urlparse
from sys import*
import os

def is_downloadable(url):
	h = request.head(url, allow_redirects = True)
	header = h.headers
	content_type = header.get('content-type')
	if 'text' in content_type.lower():
		return False
	if 'html' in content_type.lower():
		return False
	return True

def get_filename_from_cd(cd):
	a = urlparse(cd)
	return os.path.basename(a.path)

def MarvellousDownload(url):
	allowed = is_downloadable(url)

	if allowed:
		try:
			res = requests.get(url, allow_redirects = True)
			res.raise_for_status()
			filename = get_filename_from_cd(url)
			fd = open(filename, "wb")

			for buffer in res.iter_content(1024):
				fd.write(buffer)

			fd.close()
			return True
		except Exception as E:
			return False
	else:
		return False

def main():
	print("-----Downloader using Automation by Swapnil Patil-----")

    print("Application name : " +argv[0])

    if (len(argv) == 2):    
	    if (argv[1] == "-h") or (argv[1] == "-H"):
	        print("This Script is used to traverse specific directory")
	        exit()

	    if (argv[1] == "-u") or (argv[1] == "-U"):
	        print("usage : ApplicationName AbsolutePath_of_Directory")
	        exit()

    url = 'https://c1.neweggimage.com/ProductImage/14-137-632-V05.jpj'

    result = MarvellousDownload(url)

    if result:
    	print("File successfully downloader")
	else:
		print("Failed to download")

if __name__ == "__main__":
    main()


"""






"""
from sys import*
import webbrowser
import re
from urllib.request import urlopen

def is_connected():
	try:
		urlopen('http://google.com')
		return True
	except Exception as err:
		return False

def Find(string):
	url = re.findall('https[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*/(/), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
	return url


def WebLauncher(path):
	with open(path) as fd:
		for line in fd:
			url = Find(line)
			for str in url:
				webbrowser.open(str, new = 2)

def main():
    print("-----Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
    	connected = is_connected()

    	if connected:
        	WebLauncher(argv[1])
    	else:
    		print("Error : Unable to connect to internet...")

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()


"""











"""
def Create(dir):
	print("Enter the data you want to store in your file : ")
	Data = input()

	fd = open(dir,"a")
	fd.write(Data)


def main():
	print("Enter the file name that you want to create : ")
	File = input()

	Create(File)


if __name__ == "__main__":
	main()

"""




"""
import fnmatch
from sys import*
import os

def DirectoryWatcher(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    extention = input("Enter the string : \n")
    
    if exists:
        for foldername, subfolder, filname in os.walk(path):
            for filen in filname:
                if (filen == extention):
                    print(filen)
    else:
        print("Invalid Path")

def main():
    print("-----Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()


"""










"""
import os 
from sys import*

def Directory_Watcher(Dir_Name):

	flag = os.path.isabs(path)
	if flag == False:
		path = os.path.abspath(path)

	exists = os.path.isdir(path)

	print("Inside Directory Watcher method")
	print("Name of input directory : ",Dir_Name)

	for foldername, subfolder, filenames in os.walk(Dir_Name):
		print("Folder Name is : "+foldername)
		for subf in subfolder:
			print("SubFolder Name of "+foldername+" is "+subf)
		for fnames in filenames:
			print("File inside folder "+foldername+" is "+fnames+" having size "+str(os.path.getsize(fnames)))

		print(" ")

	else:
		print("Invalid Path.")

def main():
	print("Directory watcher application")

	if(len(argv) < 2):
		print("Insufficient argument")
		exit()

	if(argv[1] == "-h") or (argv[1] == "-H"):
		print("This script will travel the directory and display the names of all entries")
		exit()

	if(argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage : Application_Name Directory_Name")
		exit()

	Directory_Watcher(argv[1])

if __name__ == "__main__":
	main()

"""


"""
from sys import*
import os
import hashlib

def hashfile(path, blocksize = 1024):
	fd = open(path,'rb')
	hasher = hashlib.md5()
	buf = fd.read(blocksize)

	while len(buf) > 0:
		hasher.update(buf)
		buf = fd.read(blocksize)

	fd.close()

	return hasher.hexdigest()

def FindDuplicate(path):
	flag == os.path.isabs(path)

	if flag == False:
		path = os.path.abspath(path)

	exists = os.path.isdir(path)

	dups = {}

	if exists:
		for dirName,subdirs,fileList in os.walk(path):
			for file in fileList:
				path = os.path.join(dirName, filen)
				file_hash = hashfile(path)
				if file_hash in dups:
					dups[file_hash].append(path)
				else:
					dups[file_hash] = [path]

			return dups
		else:
			print("Invalid Path")

def PrintDuplicate(dict1):
	result = list(filter(lambda x: len(x)>1,dict1.values()))

	if len(result) > 0:
		print("Duplicates Found :")

		print("The following files are identical.")

		icnt = 0
		for result in results:
			for subresult in result:
				icnt+=1
				if icnt >= 2:
					print('\t\t%s'% subresult)
				else:
					print("No Duplicate file found.")


def main():
	print("-----Directory Watcher by Swapnil Patil-----")

	print("Application name : "+argv[0])

	if (len(argv)!= 2):
		print("Error : Invalid number of argument")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("This Script is used to traverse specific directory and display size of files.")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("usage : Application Absolutepath_of_Directory Extension.")
		exit()

	try:
		arr = {}
		arr = FindDuplicate(argv[1])
		PrintDuplicate(arr)

	except ValueError:
		print("Error : Invalid datatype of input")

if __name__ == "__main__":
	main()

"""




"""
import os

def Delete_File(FileName):
	if(os.path.exists(FileName)):
		size = os.path.getsize(FileName)
		if(size == 0):
			os.remove(FileName)
		else:
			print("Are you sure to delete the the file? Y/N")
			option = input()
			if(option == "Y") or (option == "y"):
				os.remove(FileName)
			else:
				print("File deletion process stoped.")
		
	else:
		print("There is no such file")

def main():
	print("Enter the file name to Delete")
	Name = input()

	Delete_File(Name)

if __name__ == "__main__":
	main()
"""









"""

import os

def Read_File(FileName):
	if(os.path.exists(FileName)):
		fd = open(FileName, "r")
		Data = fd.read()
		print("Data from the file is ")
		print(Data)

		fd.close()

	else:
		print("File is not existing")
		return 

def main():
	print("Enter the file name to create")
	Name = input()

	Read_File(Name)

if __name__ == "__main__":
	main()



"""

















"""
import os

def Write_File(FileName):
	if(os.path.exists(FileName)):
		print("Enter the data that you want to write in the file")
		Data = input()

		fd = open(FileName, "a")
		fd.write(Data)

	else:
		print("File is not existing")
		return 

def main():
	print("Enter the file name to create")
	Name = input()

	Write_File(Name)

if __name__ == "__main__":
	main()

"""




"""

import os

def CreateFile(FileName):
	if(os.path.exists(FileName)):
		print("File is already existing")
		return 
	else:
		fd = open(FileName,"w")

def main():
	print("Enter the file name to create")
	Name = input()

	CreateFile(Name)

if __name__ == "__main__":
	main()






"""

"""
import schedule
import time 
import datetime

def fun_Minute():
	print("Current time is ")
	print(datetime.datetime.now())
	print("Schedular executed after Minute")

def fun_Hour():
	print("Current time is ")
	print(datetime.datetime.now())
	print("Schedular executed after Hour")

def fun_Day():
	print("Current time is ")
	print(datetime.datetime.now())
	print("Schedular executed after Day")

def fun_Afternoon():
	print("Current time is ")
	print(datetime.datetiem.now())
	print("Schedular executed at 12")

def main():
	print("--------Schedular programm by Swapnil Patil--------")

	print("Python job schedular")
	print(datetime.datetime.now())

	schedule.every(1).minutes.do(fun_Minute)

	schedule.every().hour.do(fun_Hour)

	schedule.every().sunday.do(fun_Day)

	schedule.every().saturday.at("18:30").do(fun_Day)

	schedule.every().day.at("00:00").do(fun_Afternoon)

	while(True):
		schedule.run_pending()
		time.sleep(1)

if __name__ == "__main__":
	main()







"""










"""

import psutil

def ProcessDisplay():
	listprocess = []

	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid','name','username'])
			pinfo['vms'] = proc.memory_info().vms/(1024 * 1024)

			listprocess.append(pinfo);
		except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass

			return listprocess

def main():
	print("Marvellous : python Automation & Machine Learning.")

	print("Process Monitor with memory usage")

	listprocess = ProcessDisplay()

	for elem in listprocess:
		print(elem)

if __name__ == "__main__":
	main()

"""


"""
import os
import psutil
import time 
from sys import*
import os

def ProcessDisplay(log_dir = "Marvellous"):
	listprocess = []

	if not os.path.exists(log_dir):
		try:
			os.mkdir(log_dir)
		except:
			pass

	separator = "-" * 80
	log_path = os.path.join(log_dir,"MarevllousLog%s.log"%(time.ctime()))
	f = open(log_path,'W')
	f.write(separator + "\n")
	f.write("Marvellous Infosystem Process Logger : "+time.ctime()+ "\n")
	f.write(separator + "\n")

	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid','name','username'])
			vms = proc.memory_info().vms/(1024 * 1024)
			pinfo['vms'] = vms
			listprocess.append(pinfo);
		except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
			pass

	for element in listprocess:
		f.write("%s\n"% element)

def main():
	print("------------Process Monitor by Swapnil patil-----------")

	print("Application name : "+argv[0])

	if(len(argv) != 2):
		print("Error : Invalid number of arguments")
		exit()

	if(argv[1] == "-h") or (argv[1] == "-H"):
		print("This script is used log record of running processess")
		exit()

	if(argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage : ApplicationName AbsolutePath_of_Directory")
		exit()

	try:
		ProcessDisplay(argv[1])

	except ValueError:
		print("Error : Invalid datatype of input")

	except Exception:
		print("Error : Invalid input")

if __name__ == "__main__":
	main()



"""





































"""
import psutil

def ProcessDisplay():
    listprocess = [] 
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            
            listprocess.append(pinfo);
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
            
        return listprocess

def main():
    print("Marvellous Infosystem : Python Automation & Machine Learning")
    
    print("Process Monitor")
    
    listprocess = ProcessDisplay()
    
    for elem in listprocess:
        print(elem)

if __name__ == "__main__":
	main()
"""


"""
from sys import*
from os import*

def Script_Task(No):
	if ((No % 2) == 0):
		print("It is even number")
	else:
		print("It is odd number")

def main():
	print("-------Marvellous Infosystem Automation--------")

	print("Automation script started with name : ",argv[0])

	if(len(argv) != 2):
		print("Error : Insufficient argument")
		print("Use -h for help and use -u for usage of the script")
		exit()

	if(argv[1] == "-h") or (argv[1] == "-H"):
		print("Help : This script is used to perform __________")

	elif(argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage : provide _____ numebr of argument as")
		print("First Argument as :______ ")
		print("Secound Argument as :_____ ")
		exit()

	else:
		Script_Task(int(argv[1]))

if __name__ == "__main__":
	main()

"""







"""

import schedule
import time
import datetime

def Task_Minutes():
	print("Task based on minutes scheduled on : ",datetime.datetime.now())

def Task_Hour():
	print("Task based on the hour's scheduled on : ",datetime.datetime.now())

def Task_Day():
	print("Task based on the day scheduled on : ",datetime.datetime.now())

def main():
	print("Inside task scheduler : ")
	print("Current time is : ",datetime.datetime.now())

	schedule.every(1).minutes.do(Task_Minutes)
	schedule.every(1).hour.do(Task_Hour)
	schedule.every(1).monday.at("18:44").do(Task_Day)

	while(True):
		schedule.run_pending()
		time.sleep(1)

if __name__ == "__main__":
	main()
"""













"""

import schedule
import time 
import datetime
import os
import sys

Cnt = 0

def Var():
	print("Inside Variable")

def ScriptT():
	schedule.every(1).monday.at("20:18").do(Var)
	print("Inside script : ",datetime.datetime.now())

def main():
	print("Inside task schedule : ",datetime.datetime.now())

	global Cnt

	schedule.every(1).minutes.do(ScriptT)
	Cnt = Cnt + 1
	if(Cnt == 2):
		sys.exit()

	while(True):
		schedule.run_pending()
		time.sleep(1)

if __name__ == "__main__":
	main()
"""