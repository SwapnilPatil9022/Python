# Requre librarys

import pandas as pd
import matplotlib
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# import csv using pandas

data=pd.read_csv(r'kc_house_data.csv')

data.head()

# Exploratory Data Analysis
print("=================================================")
D1 = data.shape
print(D1)
print("=================================================")

print(data)
print("=================================================")

pd.set_option('display.float_format', lambda x: '%.5f' % x)

print("=================================================")

D = data.describe()
print(D)

print("=================================================")

data.info()
print(data)
 
D2 = data.isnull().sum()

print(D2)

print("=================================================")

D3 = data.columns

print(D3)

print("=======================================================")

X = data[['bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement',
        'sqft_living15', 'sqft_lot15']]

print(X)

Y = data['price']

print(Y)

print("=========================================================")

X_train, X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.25,random_state=101)

print(X_train)

print(Y_train)

print(X_test)

print(Y_test)

print("=======================================================")

# Normalization basically Standarization

std=StandardScaler()

X_train_std=std.fit_transform(X_train)
X_test_std=std.transform(X_test)

print(X_train)

print(X_train_std)

print(X_test_std)

print(Y_train)

print(Y_test)

print("========================================================")

# Model training

lr=LinearRegression()

lr.fit(X_train_std,Y_train)

Y_pred=lr.predict(X_test_std)

print(Y_pred)

print(Y_test)

print("=========================================================")

from sklearn.metrics import mean_absolute_error,r2_score

print("#########################")
mean_absolute_error(Y_test,Y_pred)
print("#########################")

print(X_test)

X_test.loc[7148]

print("==========================================")
D5 = r2_score(Y_test,Y_pred)
print(D5)
print("===========================================")

# Lets predict for Single House

new_house = [[3,1,1520,5000,1,0,0,3,8,1000,1,2000,5000]]

new_house_std = std.transform(new_house)

print(new_house_std)

Happy = (int(lr.predict(new_house_std)))
print(Happy)









"""
print("Demonstration of list")

data = [11,21,51,101]
data1 = [11,90.80,True,"Hello"]     #Hetrogenousx
"""



"""

ldata = [10,20,30,40]
tdata = (10,20,30,40)
sdata = {10,20,30,40}
ddata = {"C":400, "C++":550,"Java":900,"Python":890}

print(ldata)
print(tdata)
print(sdata)
print(ddata)

print(type(ldata))
print(type(tdata))
print(type(sdata))
print(type(ddata))

"""


"""
print("Demonstration of bulit in date types")

iobj = 11
fobj = 3.14
sobj = "Hello"
bobj = True

print(iobj)
print(fobj)
print(sobj)
print(bobj)

print(type(iobj))  
print(type(fobj))
print(type(sobj))
print(type(bobj))
ldata = [10,20,30,40]
tdata = (10,20,30,40)
sdata = {10,}

"""



"""

from sys import *

def Addition(A,B):
    Ans = 0
    Ans = A + B
    return Ans

def main():
    print("Welcome to : ",argv[0])
        
    if(argv[1] == "--U" or argv[1] == "--u"):
        print("Use the application as : ")
        print("usage : Python Name_of_Application First-number Secound_number")
        exit()

    if(argv[1] == "--H" or argv[1] == "--h"):
        print("Help : This application is used to perform addition of 2 number")
        exit()

    if(len(argv) != 3):
        print("Invalid arguments...")
        print("Please use --U or --u flag to get usage")
        print("Please enter --H or --h flag to get the usage")
        exit()

    print("Enter First number : ",argv[1])
    print("Enter secound number : ",argv[2])

    Ret = Addition(int(argv[1]),int(argv[2]))
    print("Addition is : ",int(Ret))

if __name__ == "__main__":
    main()

"""









"""

from sys import *

def Addition(A,B):
    Ans = 0
    Ans = A + B
    return Ans

def main():

    if(len(argv) != 3):
        print("Invalid arguments...")
        exit()

    print("application name is :",argv[0])

    print("Enter First number : ",argv[1])
    print("Enter secound number : ",argv[2])

    Ret = Addition(int(argv[1]),int(argv[2]))
    print("Addition is : ",int(Ret))


if __name__ == "__main__":
    main()

"""




"""
from sys import*

def main():
    print("Total number of argument are : ",len(argv))

    print("Name of application is  : ",argv[0])

    print("First argument is  : ",argv[1])
    print("Secound argument is  : ",argv[2])
    print("Third argument is : ",argv[3])

if __name__ == "__main__":
    main()
"""



"""

import Main1 as N

# def DisplayFactor(No):
#     i = 1

#     print("Factorial are : ")
#     while (i <= int(No/2)):
#         if (No % i == 0)  :
#             print(i)
#         i = i + 1

def main():
    print("Enter number : ")
    No = int(input())

    N.DisplayFactor(No)

if __name__ == "__main__":
    main()


"""


"""

def main():

    print("Enter number : ")
    No = int(input())

    print("Factorial is : ")
    for i in range(1,int(No/2)+1,1):
        if No % i == 0:
            print(i)
/
if __name__ == "__main__":
    main()

"""


"""
def main():
    print("Enter number : ")
    No = int(input())

    print("Factorial is  : ")
    i = 1

    while(i <=  (No/2)+1):
        if No % i == 0:
            print(i)
        i = i + 1

if __name__ == "__main__":
    main()

"""








"""

import os
"""
 
# install these python modules 
# pip install black isort
"""


def format(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            # if os.path.splitext(file)[1] != ".py":
                continue
            _file = os.path.join(root, file)
            os.system(f"python -m black {_file}")
            os.system(f"python -m isort {_file}")


format(".")

"""




"""    
def main():
    Arr = list()

    print("Enter how many element you want")
    size = int(input())

    print("Please enter tthe elemnet")

    for i in range(0,size):
        no = int(input())
        Arr.append(no)

    print(Arr)

if __name__ == "__main__":  z 
    main()




def main():

    Arr = list()

    print("Enter how many element you want to store")
    size = int(input())

    print("Enter the elemnet")

    i = 0

    while()




if __name__ == "__main__":
    main()
"""





"""
values =[10,20,30,40]

# for i in range(0,len(values)):
#     print(values[i])

i = 0

while(i < (len(values))):
    print(values)
    i = i + 1
"""




"""
for i in range(0,10):
    print("Jay Ganesh   ")
"""


"""
i = 0

while(i < 4):
    print("Jay Ganesh")
    i = i + 1
"""




"""
values = [10,20,30,40]
print(values)

print(type(values[1]))

values.append(50)
print(values)

values.remove(30)
print(values)

values.insert(0,90)
print(values)

# values = (10,20,30,40)
# print(values)


# values.append(50)
# print(values)

# values.remove(30)
# print(values)
"""







"""
def Maximun(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2


def main():
    print("Enter first number")
    iValue1 = int(input())

    print("Enter secound number")
    iValue2 = int(input())

    Ans = Maximun(iValue1,iValue2)
    print("Maximun value is : ",Ans)

if __name__ == "__main__":
    main()
"""















"""
import tkinter 
from tkinter import filedialog
from tkinter import *
from path import Path
import pyttsx3
from speech_recognition import Recognizer, AudioFile
 from pydub import AudioSegment
import os
from time import sleep

def takeCommand():
    global showText,go,command
    showText.delete(1.0,"end")
    showText.insert(END,"Listening....")
    
    recog = sr.Recognizer()
    command=''
    
    with sr.Microphone() as source:
        print("Listening to the user")
        recog.pause_threshold = 1
        userInput = recog.listen(source)

    try:
        print("Recognizing the command")
        command = recog.recognize_google(userInput, language ='en-in')

        print(f"Command is: {command}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize the voice.")
        return "None"
def stop():
    global go,command
    print("q pressed, exiting...")
    go = 0
    showText.delete(1.0,"end")
    showText.insert(END,command)
def audio_to_text():
    #Creating a window
    global showText
    wn2= tkinter.Tk() 
    wn2.title("TechVidvan Audio to PDF converter")
    wn2.geometry('500x500')
    wn2.config(bg='snow3')
    
    Label(wn2, text='TechVidvan Audio to Text converter',
      fg='black', font=('Courier', 15)).place(x=60, y=10)

    #Getting the PDF path input
    Label(wn2, text='Click the start and end buttons to speak and end speech').place(x=20, y=50)
    
    Button(wn2, text='Start', bg='ivory3',font=('Courier', 13),
       command=takeCommand).place(x=100, y=100)

    #Button to select the audio file and do the conversion 
    Button(wn2, text='Stop', bg='ivory3',font=('Courier', 13),
       command=stop).place(x=200, y=100)
    
    v=Scrollbar(wn2, orient='vertical')
    v.pack(side=RIGHT, fill='y')
    showText=Text(wn2, font=("Calibre, 14"), yscrollcommand=v.set)
    showText.focus()
    showText.place(x=20, y=130,width=450,height=300)
    
    v.config(command=showText.yview)
    wn2.mainloop() #Runs the window till it is closed
#text to voice
voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voice', voices[1].id)

def speak():
    global textBox
    text=textBox.get(1.0, "end-1c")
    print(text)
    voiceEngine.say(text)
    voiceEngine.runAndWait()

def text_to_audio():
    #Creating a window 
    global textBox
    wn1 = tkinter.Tk() 
    wn1.title("TechVidvan Text to Audio converter")
    wn1.geometry('500x500')
    wn1.config(bg='snow3')
    
    Label(wn1, text='TechVidvan Text to Audio converter',
      fg='black', font=('Courier', 15)).place(x=60, y=10)
    
    v=Scrollbar(wn1, orient='vertical')
    v.pack(side=RIGHT, fill='y')
    textBox=Text(wn1, font=("Calibre, 14"), yscrollcommand=v.set)
    textBox.focus()
    textBox.place(x=20, y=80,width=450,height=300)
    
    v.config(command=textBox.yview)
    Button(wn1, text="Convert", bg='ivory3',font=('Courier', 13),
       command=speak).place(x=230, y=400)
    
    wn1.mainloop()
wn = tkinter.Tk() 
wn.title("PythonGeeks Text to Audio and Audio to Text converter")
wn.geometry('700x300')
wn.config(bg='LightBlue1')
  
Label(wn, text='TechVidvan Text to Audio and Audio to Text converter',
      fg='black', font=('Courier', 15)).place(x=40, y=10)

global textBox,showText,command,go
go=1

Button(wn, text="Convert Text to Audio", bg='ivory3',font=('Courier', 15),
       command=text_to_audio).place(x=230, y=80)
Button(wn, text="Convert Audio to Text", bg='ivory3',font=('Courier', 15),
       command=audio_to_text).place(x=230, y=150)

wn.mainloop()

"""













"""
# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3 

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command) 
	engine.runAndWait()
	
	
# Loop infinitely for user to
# speak

while(1): 
	
	# Exception handling to handle
	# exceptions at the runtime
            	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level 
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for the user's input 
			audio2 = r.listen(source2)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("Did you say ",MyText)
			SpeakText(MyText)
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occurred")



"""






"""
import speech_recognition as sr
import os
import pyttsx3

def say():
	engine = pyttsx3.init() 
	text = "Python is a great programming language"  
	engine.say(text)  
	# play the speech  
	engine.runAndWait() 

def main():
	say()

if __name__ == "__main__":
	main()
	print("Hello Shree...")
	print("Hello I am your assistance.")

"""



  
# initialize Text-to-speech engine  
 
# convert this text to speech  
 