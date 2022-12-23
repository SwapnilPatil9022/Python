"""
 Code : This Automation script is accept the .xlsx file dataframe and encoding the data and dispay and store 
        the scatterplot daigram using matplotlib. 
        This daigram is send perodiclly using sheduler through the mail. 
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
    Reciever_Email = 'marvellousinfosystems@gmail.com'
    Password = 'xvfxeadltnyzbnoj' 

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
