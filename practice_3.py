
# import librarys
import pandas as pd
from sklearn import tree

# Load the dataset
# Rough 1
# Smooth 0

# Tennis 1
# Cricet 2

Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

# Deside the MAchine learnig algoritham
obj = tree.DecisionTreeClassifier()

# Perform the trenning model
obj = obj.fit(Features,Labels)

# perform the testing 
print(obj.predict([[97,0]])






















"""

from sys import*
import os
import hashlib
import time

def DeleteFiles(dict):
	results = list(filter(lambda x : len(x) > 1, dict.values()))

	icnt = 0;

	if len(results) > 0:
		for result in results:
			for subresult in result:
				icnt += 1
				if icnt >= 2:
					os.remove(subresult)
				icnt = 0
			else:
				print("No duplicate files found.")

def hashfile(path, blocksize = 1024):
	afile = open(path, 'rb')
	hasher = hashlib.md5()
	buf = afile.read(blocksize)

	while len(buf)

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
	print("Process Moniter")

	listprocess = ProcessDisplay()

	for elem in listprocess:
		print(elem)

if __name__ == "__main__":
	main()
"""



















"""
import os 
from sys import*

def Directory_Watcher(Dir_Name):
	print("Inside Directory Watcher method")
	print("Name of input directory : ",Dir_Name)

	for foldername, subfolder, filenames in os.walk(Dir_Name):
		print("Folder Name is : "+foldername)
		for subf in subfolder:
			print("SubFolder Name of "+foldername+" is "+subf)
		for fnames in filenames:
			print("File inside folder "+foldername+" is "+fnames)
		print(" ")

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
import os
from sys import*

def Directory_Watcher(path):
	flag = os.path.isabs(path)
	if flag == False:
		path = os.path.abspath(path)

	exists = os.path.isdir(path)

	if exists:
		for foldername, subfolder, Filenames in os.walk(path):
			# print("foldernameder name is : "+foldername)
			# for subf in subfolder:
				# print("Subfolder name of "+foldername+" is "+subf)
			for fname in Filenames:
				print("File inside folder "+foldername+" is "+fname+ "having size"+ str(os.path.getsize(fname)))
			print(" ")
	else:
		print("Invalid path")

def main():
	print("Directory watcher application")

	if (len(argv) != 2):
		print("Error : Invalid number of argument")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Help : this script will travel the directory and display the numes os all entries.")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage : Application_name Directory_Name")
		exit()

	Directory_Watcher(argv[1])

if __name__ == "__main__":
	main()

"""



















"""
import os

def Delet_File(FileName):
	if(os.path.exists(FileName)):
		size = os.path.getsize(FileName)
		if (size == 0):
			os.remove(FileName)
		else:
			print("Are you sure delete the file ? Y/N")
			option = input()
			if (option == "Y") or (option == "y"):
				os.remove(FileName)
			else:
				print("File deleting process stoped")

	else:
		print("There is no such file")

def main():
	print("Enter the file name to create")
	Name = input()

	Delet_File(Name)

if __name__ == "__main__":
	main()
"""


















"""
import os

def Delet_File(FileName):
	if(os.path.exists(FileName)):
		os.remove(FileName)
	else:
		print("There is no such file")
		

def main():
	print("Enter the file name to create")
	Name = input()

	Delet_File(Name)

if __name__ == "__main__":
	main()
"""
















"""
import os

def Read_File(FileName):
	if(os.path.exists(FileName)):
		fd = open(FileName,'r')
		Data = fd.read()
		print("Data form the file is ")
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
	if (os.path.exists(FileName)):
		print("File is alredy exsisting")
		return 
	else:
		fd = open(FileName, 'w')

def main():
	print("Enter the file name to create")
	Name = input()

	CreateFile(Name)

if __name__ == "__main__":
	main()
"""









"""
import os
import time
import psutil
from sys import*

def ProcessDisplay(log_dir = "Process_log_file"):
	listprocess = []

	if not os.path.exists(log_dir):
		try:
			os.mkdir(log_dir)
		except:
			pass

	separator = "-" * 80
	log_path = os.path.join(log_dir,"Process_log_fileLog%s.log" %(time.ctime()))
	f = open(log_path,'w')
	f.write(separator + "\n")
	f.write("Process Logger : "+time.ctime() + "\n")
	f.write(separator + "\n")

	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(atts=['pid','name','username'])
			vms = proc.memory_info().vms / (1024 * 1024)
			pinfo['vms'] = vms
			listprocess.append(pinfo);
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass

	for element in listprocess:
		f.write("%s\n" % element)

def main():
	print("Python Automation & Machine Learning")

	print("Process Monitor")

	print("Application Name : " +argv[0])

	if (len(argv) != 2):
		print("Error : Invalid number of argument")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Help : this script is used log recourd or running procesess")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage : Application AbsolutePath_of_Directory")
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
	print("Python Automation & Machine Learning")

	print("Process Monitor")

	listprocess = ProcessDisplay()

	for elem in listprocess:
		print(elem)

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

		except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
			pass

		return listprocess
def main():
	print("-----Python Automation & Machine lerning-----")

	print("Process Moniter")

	listprocess = ProcessDisplay()

	for elem in listprocess:
		print(elem)

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

def  Script_Task(No):
	if ((No % 2) == 0):
		print("It is even number")
	else:
		print("Its odd numebr")

def main():
	print("Automation script started with name : ",argv[0])

	if (len(argv) != 2):
		print("Error : Insufficent Argument")
		print("Use -h for help and use -u for usage of the script")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Help : This script is used to perform__________")
		exit()

	if (((argv[1]) == "-u") or (argv[1] == "-U")):
		print("Usage : provide _____ number of Argument")
		print("First Argument as : _____")
		print("Secound Argument as : ______")
		exit()

	else:
		Script_Task(int(argv[1]))

if __name__ == "__main__":
	main()
"""




















"""
import time
import schedule
import datetime

def Fun():
    print("----Inside Fun at a time----: ",datetime.datetime.now())
    
def script_terminator():
	schedule.every(1).minutes.do(Fun)
	schedule.every().monday.at("14:27").do(script_terminator1)

def script_terminator1():
	schedule.every().monday.at("14:28").do(terminate)

def terminate():
	exit()

def main():
	print("Inside Main",datetime.datetime.now())

	schedule.every().monday.at("14:24").do(script_terminator)

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

def Task_min():
	print("Task min",datetime.datetime.now())

def Task_Hour():
	print("Task Hour",datetime.datetime.now())
	
def Task_day():
	print("Task day",datetime.datetime.now())


def main():
	print("Inside Main",datetime.datetime.now())

	schedule.every(1).minutes.do(Task_min)
	schedule.every(1).hour.do(Task_Hour)
	schedule.every().monday.at("13:31").do(Task_day)

	while(True):
		schedule.run_pending()
		time.sleep(1)

if __name__ == "__main__":
	main()

"""



















"""

import time
import datetime
import schedule

def Fun():
    print("Inside Fun at a time : ",datetime.datetime.now())
    
def main():
    print("Inside task scheduler")
    print("Current time is : ", datetime.datetime.now())

    schedule.every(1).minutes.do(Fun)

    while(True):
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()
"""

























"""
import time
import datetime
import schedule

def Fun():
    print("Inside Fun")
    
def main():
    print("Inside task scheduler")

    schedule.every(1).minutes.do(Fun)

    while(True):
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()

"""

















"""
def Add(No):
    if(No <= 0):
        return 0
    else:
        return (No  + Add((No-1))
        
Ret = Add(3)

print("Result is : ",Ret)
"""

















"""
def Display(No):
    i = 0
    while(No <= 0):
        print(No)
        i = i + No
        print(No)
        
def main():
    Display(9)

if __name__ == "__main__":
    main()
"""


















"""
def Add(No):
    Ans = 0
    while(No >= 0):
        
        No = No - 1
        Ans = Ans - No
    return Ans
    
Ret = Add(4)
print("Reesult is :",Ret)
"""














"""
def Display(No):
    if(No > 0):
        print("Hello")
        No = No - 1
        Display(No) #Recursive function call
        print(4)
        
Display(4)  # function call

"""















"""
import sys

print(sys.getrecursionlimit())

sys.setrecursionlimit(3001)

print(sys.getrecursionlimit())
"""







"""
def Display(No):
    Cnt = 0
    
    while(Cnt < No):
        print("Hello")
        Cnt = Cnt + 1
        Display(No)
        
Display(4)
"""



















"""

def Display(No):
    Cnt = 0
    
    while(Cnt < No):
        print("Hello")
        Cnt = Cnt + 1
        
Display(4)
"""




























"""
def Substraction(No1,No2):
    Ans = 0
    Ans = No1 - No2
    return Ans
    
def Decorated_Function(Function_Name):
    def Inner(A,B):
        if (A < B):
            A,B = B,A
        return Function_Name(A,B)
    return Inner
    
def main():
   Value1 = int(input("Enter First number\n"))
   Value2 = int(input("Enter Secound number\n"))
   
   New_Function = Decorated_Function(Substraction)
   print(New_Function(Value1,Value2))
   
if __name__ == "__main__":
    main()
"""




















"""
def Add(A,B):
    return A+B
    
def Sub(A,B):
    return A-B
    
def Calculater(Target, Value1, Value2):
    return Target(Value1,Value2)
    
Ret = Calculater(Target = Add, Value1 = 10, Value2 = 11)
print("Addition is :",Ret)

Ret = Calculater(Target = Sub, Value1 =  10, Value2 = 11)
print("Substarction is :",Ret)
"""






















"""
def Demo():
    print("Inside Demo")
    
def Fun():
    print("Inside fun")
    
def Hello(FPTR,F1):
    print("Insdie Hello")

    FPTR()
    F1()
    
Hello(Demo,Fun)
"""


















"""
def main():
    try :
        print("Enter first numebr")
        No1 = int(input())
        
        print("Enter secound number")
        No2 = int(input())
    

        Ans = No1 / No2
        print("Division is :",Ans)
    except ZeroDivisionError:
        print("inside ZeroDivisionError")
    except ValueError:
        print("inside Value Error:")
    except Exception:
        print("Inside last except block")
    finally:
        print("Inside finally block")

if __name__ == "__main__":
    main()
"""

























"""
import time
import multiprocessing
import threading 

def DisplayEven(No):
    for i in range(1,No,1):
        if (i % 2 == 0):
            print("Even number :",i)

def DisplayOdd(No):
    for i in range(1,No,1):
        if (i % 2 != 0):
            print("Even number :",i)
def main():
    print("Demonstration of parallel programing using multiple processes")
    Number = 20
    
    p1 = multiprocessing.Process(target = DisplayEven, args = (Number,))
    p2 = multiprocessing.Process(target = DisplayOdd, args = (Number,))
    print("------------------------------------------------------------")
    p1 = threading.Thread(target = DisplayEven, args = (Number,))
    p2 = threading.Thread(target = DisplayOdd, args = (Number,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is :",end_time - start_time)

"""


























"""
import time
import multiprocessing

def DisplayEven(No):
    for i in range(1,No,1):
        if (i % 2 == 0):
            print("Even number :",i)

def DisplayOdd(No):
    for i in range(1,No,1):
        if (i % 2 != 0):
            print("Even number :",i)
def main():
    print("Demonstration of parallel programing using multiple processes")
    Number = 20000000
    
    p1 = multiprocessing.Process(target = DisplayEven, args = (Number,))
    p2 = multiprocessing.Process(target = DisplayOdd, args = (Number,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is :",end_time - start_time)
"""



























"""
import time
import multiprocessing

def DisplayEven(No):
    for i in range(1,No,1):
        if (i % 2 == 0):
            print("Even number :",i)

def DisplayOdd(No):
    for i in range(1,No,1):
        if (i % 2 != 0):
            print("Even number :",i)
def main():
    print("Demonstration of parallel programing using multiple processes")
    Number = 200
    
    p1 = multiprocessing.Process(target = DisplayEven, args = (Number,))
    p2 = multiprocessing.Process(target = DisplayOdd, args = (Number,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is :",end_time - start_time)
"""



























"""
import time

def DisplayEven(No):
    for i in range(1,No,1):
        if (i % 2 == 0):
            print("Even number :",i)

def DisplayOdd(No):
    for i in range(1,No,1):
        if (i % 2 != 0):
            print("Even number :",i)
def main():
    DisplayEven(2000)
    print("-------------------")
    DisplayOdd(2000)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("Execution time is :",end_time - start_time)
"""

















"""
import os

import multiprocessing 

def Square(No):
    print("PID of worker process is {} for the input {}".format(os.getpid(), No))
    return (No*No)

def main():
    print("Process ID of our application is : ",os.getpid())
    
    Data = [1,2,3,4,5]
    Result = []
    
    pobj = multiprocessing.Pool()
    
    Result = pobj.map(Square, Data)
    
    print("Result after square opretion is : ",Result)
    
if __name__ == "__main__":
    main()
"""
























"""

def Square(No):
    return (No*No)

def main():
    Data = [1,2,3,4,5]
    Result = []
    
    for Value in Data:
        Result.append(Value)
        
    print("Result of square :",Result)
    
if __name__ == "__main__":
    main()
"""
















"""
import os

def main():
    print("PID of current process is :",os.getpid())
    print("PID of parent process is :",os.getppid())
    
if __name__ == "__main__":
    main()
"""














"""
import multiprocessing

def main():
    print("Number of core are : ",multiprocessing.cpu_count())
    
if __name__ == "__main__":
    main()

"""





















"""
# Instance Variable : Name, Amount , Address, Accountno
# Instance Method  : CreteAccount(), DisplayAccountInfo()

class Bank_Account:

    Bank_Name = "HDFC bank PVT LTD"
    ROI_On_FD = 6.7

    def __init__(self):
        self.Name = " "
        self.Amount = 0
        self.Address = " "
        self.AccountNo = 0
        
    def CreateAccount(self):
        print("Enter your name : ")
        self.Name = (input())

        print("Enter your initial amount : ")
        self.Amount = int(input())
        
        print("Enter your Address : ")
        self.Address = input()
        
        print("Enter your Account number  : ")
        self.AccountNo = int(input())
        
    def DisplayAccountInfo(self):
        print("----Your accouunt information in below------")
        print("Name of account holder : ",self.Name)
        print("Account number : ",self.AccountNo)
        print("Address of account holder :",self.Address)
        print("Currnrt Amount of account :",self.Amount)
        print("------------------------------------------------")
        
    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to bank console")
        print("Name of our bank is : ",cls.Bank_Name)
        print("Rate of intrest we offer on fixed deposit is : ",cls.ROI_On_FD)
        print("------------------------------------------------")
        
    @staticmethod
    def DisplayKYCInfo():
        print("KYC information")
        print("1 : clear passport size photo")
        print("2 : photo of aadhar card")
        print("3 : Photo of pan card")
        print("------------------------------------------------")
def main():
    
    User1 = Bank_Account()
    User2 = Bank_Account()
    
    print("----------Account holder 1 :---------")
    User1.CreateAccount()
    print("----------Account holder 2 :---------")
    User2.CreateAccount()
    
    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()
    User1.DisplayKYCInfo()
    
    User1.DisplayBankInformation()
    User2.DisplayBankInformation()    
    User2.DisplayKYCInfo()
    
if __name__ == "__main__":
    main()
"""

























"""
class Numbers:
	def __init__(self):
		self.Size = 0
		self.Arr = list()
		self.No = 0

	def Accept(self):
		print("Enter how many element you want ")
		self.Size = int(input())

		print("Please enter the elements")
		Value = 0
		for i in range(0,self.Size,1):
			Value = int(input())
			self.Arr.append(Value)

	def Display(self):
		print("elements from list are : ")

		for i in range(0,self.Size):
			print(self.Arr[i], end = " ")

	def Summation(self):
		Sum = 0
		for i in range(0,self.Size):
			Sum = Sum + self.Arr[i]

		return Sum

	def Avrage(self):
		Sum = 0
		for i in range(0,self.Size):
			Sum = Sum + self.Arr[i]

		return (Sum/self.Size)

	def Maximum(self):
		Max = self.Arr[0]
		for i in range(0,self.Size):
			if (self.Arr[i] > Max):
				Max = self.Arr[i]

		return Max

	def Minimum(self):
		Min = self.Arr[0]
		for i in range(0,self.Size):
			if (self.Arr[i] < Min):
				Min = self.Arr[i]

		return Min

	def CheckPrime(self):
		i = 0
		Flag = Ture

		for i in range(0,int(self.Size/2)+1):
			if (self.No % i == 0):
				Flag = False
				break

		if (i == int(self.No/2)):
			return True
		else:
			return False


def main():
	obj = Numbers()
	obj.Accept()
	obj.Display()

	Output = obj.Summation()
	print("\n Summation of all elements : ",Output)

	Output = obj.Avrage()
	print("\n Avrage of all elements : ",Output)

	Output = obj.Maximum()
	print("\n Maximum of all elements : ",Output)

	Output = obj.Minimum()
	print("\n Minimum of all elements : ",Output)

if __name__ == "__main__":
	main()
"""






















"""
from functools import reduce



















CheckEven = lambda No : (No % 2 == 0)

Multiplication = lambda No : No*2

Sum = lambda A,B : A+B

def main():
	print("Please enter the number that you want to store in list")
	iSize = int(input())

	Data_Input = []
	print("Enter the numbers")
	for iCnt in range(0,iSize,1):
		Value = int(input())
		Data_Input.append(Value)

	print("Data set is of list : ",Data_Input)

	Data_Filter = list(filter(CheckEven, Data_Input))
	print("Data after filter :",Data_Filter)	

	Data_Map = list(map(Multiplication, Data_Filter))
	print("Data after map :",Data_Map)

	Data_reduce = (reduce(Sum, Data_Map))
	print("Data after reduce :",Data_reduce)

if __name__ == "__main__":
	main()
"""























"""

from functools import reduce

CheckEven = lambda No: (No % 2 == 0)

Multiplication = lambda No : (No*2)

Sum = lambda A,B : A+B

def main(): 
	print("How many element that you wnat to store")
	iSize = int(input())

	Data_Input = []
	print("Enter the data")
	for iCnt in range(0,iSize,1):
		Value = int(input())
		Data_Input.append(Value)

	print("Dataset is : ",Data_Input)

	Data_Filter = list(filter(CheckEven, Data_Input))
	print("Data after filter : ", Data_Filter)

	Data_Map = list(map(Multiplication, Data_Filter))
	print("Data after map : ", Data_Map)

	Data_reduce = (reduce(Sum, Data_Map))
	print("Data after map : ", Data_reduce)

if __name__ == "__main__":
	main()
"""






































"""
def CheckEven(No):
	return (No % 2 == 0)

def Multiplication(No):
	return (No*2)

def Sum(A,B):
	return A+B

def reduceX(Helper_Function, Data):
	Ans = 0
	for i in Data:
		Ans = Helper_Function(Ans, i)
	return Ans

def filterX(Helper_Function, Data):
	
	Result = []
	for i in Data:
		if (Helper_Function(i) == True):
			Result.append(i)
	return Result

def mapX(Helper_Function, Data):

	Result = []

	for i in Data:
 		Value = Helper_Function(i)
 		Result.append(Value)
	return Result

def main(): 
	print("How many element that you wnat to store")
	iSize = int(input())

	Data_Input = []
	print("Enter the data")
	for iCnt in range(0,iSize,1):
		Value = int(input())
		Data_Input.append(Value)

	print("Dataset is : ",Data_Input)

	Data_Filter = list(filterX(CheckEven, Data_Input))
	print("Data after filter : ", Data_Filter)

	Data_Map = list(mapX(Multiplication, Data_Filter))
	print("Data after map : ", Data_Map)

	Data_reduce = (reduceX(Sum, Data_Map))
	print("Data after map : ", Data_reduce)

if __name__ == "__main__":
	main()
"""
























"""
from functools import reduce

CheckEven = lambda No : (No % 2 == 0)

Double = lambda No : No*2

Sum = lambda A,B : A+B

def main():
	print("Enter number of element you want to enter : ")
	iSize = int(input())

	Data_Input = []
	print("Please enter the data ")
	for iCnt in range(0,iSize,1):
		Value = int(input())
		Data_Input.append(Value)

	print("Data is  :",Data_Input)

	Data_Filter = list(filter(CheckEven, Data_Input))
	print("Data after filter is : ",Data_Filter)

	Data_Map = list(map(Double,Data_Filter))
	print("Data after map is : ",Data_Map)

	Data_Reduce = reduce(Sum, Data_Map)
	print("Data after reduce is : ",Data_Reduce)

if  __name__ == "__main__":
	main()
"""






























"""
CheckEven = lambda No : (No % 2 == 0)


Double = lambda No : No*2


Sum = lambda A,B : A+B

def filterX(Helper_Function, Data):
	Result = []
	for no in Data:
		if(Helper_Function(no) == True):
			Result.append(no)

	return Result

def mapX(Helper_Function, Data):
	Result = []
	for No in Data:
		Value = Helper_Function(No)
		Result.append(Value)

	return Result

def reduceX(Helper_Function, Data):
	Ans = 0
	for no in Data:
		Ans = Helper_Function(Ans,no)

	return Ans

def main():
	print("Enter number of element you want to enter : ")
	iSize = int(input())

	Data_Input = []
	print("Please enter the data ")
	for iCnt in range(0,iSize,1):
		Value = int(input())
		Data_Input.append(Value)

	print("Data is  :",Data_Input)

	Data_Filter = filterX(CheckEven, Data_Input)
	print("Data after filter is : ",Data_Filter)

	Data_Map = mapX(Double,Data_Filter)
	print("Data after map is : ",Data_Map)

	Data_Reduce = reduceX(Sum, Data_Map)
	print("Data after reduce is : ",Data_Reduce)

if  __name__ == "__main__":
	main()
"""








































"""
def CheckEven(No):
	return (No % 2 == 0)

# ChkEven = lambda No : (No % 2 == 0)

def Double(No):
	return No*2

# Double = lambda No : No*2

def Sum(A,B):
	return A+B

# Sum = lambda A,B : A+B

def filterX(Helper_Function, Data):
	Result = []
	for no in Data:
		if(Helper_Function(no) == True):
			Result.append(no)

	return Result

def mapX(Helper_Function, Data):
	Result = []
	for No in Data:
		Value = Helper_Function(No)
		Result.append(Value)

	return Result

def reduceX(Helper_Function, Data):
	Ans = 0
	for no in Data:
		Ans = Helper_Function(Ans,no)

	return Ans

def main():
	print("Enter number of element you want to enter : ")
	iSize = int(input())

	Data_Input = []
	print("Please enter the data ")
	for iCnt in range(0,iSize,1):
		Value = int(input())
		Data_Input.append(Value)

	print("Data is  :",Data_Input)

	Data_Filter = filterX(CheckEven, Data_Input)
	print("Data after filter is : ",Data_Filter)

	Data_Map = mapX(Double,Data_Filter)
	print("Data after map is : ",Data_Map)

	Data_Reduce = reduceX(Sum, Data_Map)
	print("Data after reduce is : ",Data_Reduce)

if  __name__ == "__main__":
	main()
"""















"""

def chkEven(No):
	return (No % 2 == 0)

def Increment(No):
	return No+2

def filter(Arr,Function_name):
	Result = []
	for no in Arr:
		if (Function_name(no)):
			Result.append(no)
	return Result

def map(Arr,Function_name):
	Result = []
	for no in Arr:
		value = (Function_name(no))
		Result.append(value)
	return Result

def reduce(Arr):
	Sum = 0
	for no in Arr:
		Sum = Sum + no
	return Sum

def main():
	Data = [2,3,1,6,4,5,11,16,20]
	print("Orignal data : ",Data)

	Data_filter = list(filter(Data,chkEven))
	print("Data after filter is :",Data_filter)

	Data_map = list(map(Data_filter,Increment))
	print("Data after maping is :",Data_map)

	Ret = reduce(Data_map)

	print("Data after reduce :",Ret)

if __name__ == "__main__":
	main()

"""

































"""
def chkEven(No):
	return (No % 2 == 0)

def Increment(No):
	return No+2

def filterX(Arr,Function_name):
	Result = []
	for no in Arr:
		if (Function_name(no)):
			Result.append(no)
	return Result

def mapX(Arr,Function_name):
	Result = []
	for no in Arr:
		value = (Function_name(no))
		Result.append(value)
	return Result

def reduceX(Arr):
	Sum = 0
	for no in Arr:
		Sum = Sum + no
	return Sum

def main():
	Data = [2,3,1,6,4,5,11,16,20]
	print("Orignal data : ",Data)

	Data_filter = list(filterX(Data,chkEven))
	print("Data after filter is :",Data_filter)

	Data_map = list(mapX(Data_filter,Increment))
	print("Data after maping is :",Data_map)

	Ret = reduceX(Data_map)

	print("Data after reduce :",Ret)

if __name__ == "__main__":
	main()
"""


















"""

Even = lambda No : No % 2 == 0 

def main():
	Ret = Even(11)

	if (Ret == True):
		print("Its even")
	else:
		print("Its odd")
if __name__ == "__main__":
	main()
"""
















"""
def Add1(No1,No2):
	return No1+No2

Add2 = lambda A,B : A+B

Ans1 = Add1(10,12)
print("Addition is :",Ans1)

Ans2 = Add1(10,12)
print("Addition is :",Ans2)

"""






















"""
def Add(*Values):
	Sum  = 0
	for no in Values:
		Sum = Sum + no

	return Sum

def AddX(*Values):
	Sum  = 0
	for i in range(0,len(Values)):
		Sum = Sum + Values[i]

	return Sum

def main():

	Ans = Add(1,7,9,4,6,5)
	print("Addition is : ",Ans)
	print("--------------------")

	Ans = AddX(1,7,9,4,6,5)
	print("Addition is : ",Ans)
	print("--------------------")

if __name__ == '__main__':
	main()
"""


























"""
def Area(Radius, PI = 3.14):
	Result = PI * Radius * Radius
	return Result

def main():
	Rvalue = 10.5
	PIvalue = 3.14

	Ans = Area(Rvalue,PIvalue)
	print("Addition is : ",Ans)
	print("--------------------")
	Ans = Area(Radius = Rvalue,PI = PIvalue)
	print("Addition is : ",Ans)
	print("--------------------")
	Ans = Area(10.5)
	print("Addition is : ",Ans)
	print("--------------------")
	Ans = Area(Radius = 7.10,PI = 10.5)
	print("Addition is : ",Ans)
	print("--------------------")

if __name__ == '__main__':
	main()
"""

















"""
# positional Argument

def Add1(No1, No2):
	print("Value of No1 :",No1)
	print("Value of No1 :",No2)
	return No1 + No2

def Sub1(No1, No2):
	print("Value of No1 :",No1)
	print("Value of No1 :",No2)
	return No1 - No2

def main():
	Ans = 0
	Ans = Add1(10,11)
	print("Addition is : ",Ans)
	print("--------------------")
	Ans = Sub1(No1 = 10,No2 = 11)
	print("Addition is : ",Ans)
	print("--------------------")
	Ans = Sub1(No2 = 10,No1 = 11)
	print("Addition is : ",Ans)

if __name__ == '__main__':
	main()
"""

















"""
Data = {10 : "A",20: "B",30: "C",40: "D",50 : "E"}

print("Output using for")

for x in Data:
	print(x)

for x in Data:
	print(x,Data[x])

for x in Data:
	print(x,Data.get(x))
"""











"""
data1 = [10,20,30,40,50]
data2 = (10,20,30,40,50)
data3 = {10,20,30,40,50}
data4 = {10 : "A",20: "B",30: "C",40: "D",50 : "E"}

print(type(data1))
print(type(data2))
print(type(data3))
print(type(data4))
"""





















"""
  * Above data set contains information about Head and Brain size depends on gender and age.
	
	Consider below characteristics of Machine Learning Application.

	Classifier : 	Linear Regression
	Dataset :  		HeadBrain Dataset
	Features :		Gender, Age, Head size, Brain weight
	Labels : 		-
	Training Dataset : 237

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


"""





















"""
 4.5 Writer a program which accept number from user and return display between summation of all factors and non factors.

 	Input : 12
 	Output : -34	(16 - 50)

	Input  : 10
	Output : -29	(8 - 37)

def DisplayDiffSum(No):
	cnt = 0
	mult = 1

	for i in range(1,No+1):
		if (No % i) != 0:
			print(i)
			cnt = cnt + i
	print(cnt)
		
	print("\n--------------\n")

	cnt1 = 0
	for i in range(1,No):
		if No % i == 0:
			print(i)
			cnt1 = cnt1 + i
	print(cnt1)

	result = cnt1 - cnt
	print("Result is ",result)
	
def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayDiffSum(Value)

if __name__ == "__main__":
	main()

"""































"""
 4.4 Writer a program which accept number from user and display summation of all non factors.

 	Input : 12
 	Output : 50

	Input  : 10
	Output : 37

def DisplayNonFact(No):

	cnt = 0
	
	for i in range(1,No+1):
		if No % i != 0:
			print(i ,"+", end = " ")
			cnt = cnt + i
	print("\n")
	print("summation of all non factors : ",cnt)
	
def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayNonFact(Value)

if __name__ == "__main__":
	main()
"""

























"""
 4.3 Writer a program which accept number from user and display all non factors.

 	Input : 12
 	Output : 5	7	8	9	10	11 

	Input  : 10
	Output : 3	4	6	7	8	9

def DisplayNonFact(No):
	
	for i in range(1,No+1):
		if No % i != 0:
			print(i, end = " ")
	
def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayNonFact(Value)

if __name__ == "__main__":
	main()
"""





















"""
 4.1 Writer a program which accept number from user and display its factors in decressing order.

 	Input : 12
 	Output : 6 4 3 2 1 

	Input  : 10
	Output : 5 2 1

def DisplayFactRev(No):
	
	cnt = 0

	for i in range(No-1,0,-1):
		if No % i == 0:
			print(i, end= " ")
			cnt = i - cnt

def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayFactRev(Value)

if __name__ == "__main__":
	main()

"""



























"""

 4.1 Writer a program which accept number from user and display its multiplication of factors.

 	Input : 12
 	Output : 144	(1*2*3*4*6)

	Input  : 13
	Output : 1		(1)

def DisplayFact(No):
	
	cnt = 0
	Mult = 1

	for i in range(1,No):
		if No % i == 0:
			print(i)
			cnt = cnt + i
			Mult = i * Mult

	print("multiplication of factors :",Mult)

def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayFact(Value)

if __name__ == "__main__":
	main()

"""
















"""
def DisplayNum(No):
	
	if (No == 'a') or (No == 'e') or (No == 'i') or (No == 'o') or (No == 'u'):
		print(True)
	else:
		print(False)

def main():
	print("Please enter the number :")
	Value = (input())

	DisplayNum(Value)

if __name__ == "__main__":
	main()

"""

















"""
def DisplayNum(No):
	print(No.lower())

	print(No.upper())

def main():
	print("Please enter the number :")
	Value = (input())

	DisplayNum(Value)

if __name__ == "__main__":
	main()

"""
















"""
def DisplayNum(No):

	for i in range(1,No+1):
		if No % i == 0:
			if i % 2 == 0:
				print(i)

def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayNum(Value)

if __name__ == "__main__":
	main()

"""











"""
def DisplayNum(No):

	for i in range(1,No+1):
		if No % i == 0:
			print(i)

def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayNum(Value)

if __name__ == "__main__":
	main()
"""












"""

def DisplayNum(No):

	for i in range(1,No*2):
		if (i % 2) == 0:
			print(i)


def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayNum(Value)

if __name__ == "__main__":
	main()

"""














"""
def Display(No1,No2):
	for i in range(0,No2):
		print(No1, end = " ")

def main():
	print("----Application  program-----")

	value1 = int(input("Enter the number\n"))
	value2 = int(input("Enter the number\n"))

	Display(value1,value2)

if __name__ == "__main__":
	main()
"""

















"""
def Display(No1):
	if No1 <= 10:
		print("Hello")
	else:
		print("Demo")

def main():
	print("----Application  program-----")

	value = int(input("Enter the number\n"))

	Display(value)

if __name__ == "__main__":
	main()
"""

















"""
def Display(No1, No2):
	Ans =  No1 / No2
	print(Ans)

def main():
	print("----Application  program-----")

	value1 = int(input("Enter the first number\n"))
	value2 = int(input("Enter the secound number\n"))

	Display(value1,value2)

if __name__ == "__main__":
	main()
"""












"""

#  Assignment 1.10

def Display(string):
	count = 0

	for i in range(0,len(string)):
		if(string[i] != ''):
			count = count + 1

	print("Total number of chararacter : " +str(count))

def main():
	print("----Application  program-----")

	value = (input("Enter the string\n"))

	Display(value)

if __name__ == "__main__":
	main()

"""















"""
#  Assignment 1.9

def Display(No1):
	for i in range(2,20+1,2):
		if i % 2 == 0:
			print(i, end= " ")

def main():
	print("----Application  program-----")

	value = int(input("Enter the number\n"))

	Display(value)

if __name__ == "__main__":
	main()

"""



















"""
#  Assignment 1.8

def Display(No1):
	s = "*"

	for i in range(1,No1+1):
		i = i + 1
		print(s, end=" ")

def main():
	print("----Application  program-----")

	value = int(input("Enter the number\n"))

	Display(value)

if __name__ == "__main__":
	main()

"""














"""
#  Assignment 1.7

def Display(No1):
	
	if No1 % 5 == 0:
		print("True")
	else:
		print("False")

def main():
	print("----Application  program-----")

	value = int(input("Enter the number\n"))

	Display(value)

if __name__ == "__main__":
	main()

"""













"""
#  Assignment 1.6

def Display(No1):
	
	if No1 == 0:
		print("Zero")
	elif No1 > 0:
		print("Positive number")
	else:
		print("Negative number")

def main():
	print("----Application  program-----")

	value = int(input("Enter the number\n"))

	Display(value)

if __name__ == "__main__":
	main()
"""

















"""
#  Assignment 1.5

def Display():
	print("Display using for loop")
	for i in range(10,0,-1):
		print(i, end = " ")

	print("\n")

	print("'Display using while loop")
	i = 10
	while i >= 1:
		print(i, end= " ")
		i = i - 1

def main():
	print("----Application  program-----")

	Display()

if __name__ == "__main__":
	main()

"""












"""

# Assignment 1.4

def Display():
	print("Display using for loop")
	for i in range(5,0,-1):
		print("Marvellous")

	print("\n")

	print("'Display using while loop")
	i = 5
	while i >= 1:
		print("Marvellous")
		i = i - 1

def main():
	print("----Application  program-----")

	Display()

if __name__ == "__main__":
	main()

"""














"""
# 2 Assignment 1.3

def Add(No1, No2):

	Ans = (No1 + No2)
	return Ans

def main():
	print("----Application of addition program-----")

	Value1 = int(input("Enter the first number :\n"))
	Value2 = int(input("Enter the secound number :\n"))

	result = Add(Value1, Value2)
	print("Addition is : ",result)

if __name__ == "__main__":
	main()
"""


















"""
# 2 Assignment 1.2

def ChkEven(No1):
	print("Inside Chkeven function")

	if No1 % 2 == 0:
		print("Even number")
	else:
		print("Odd number")

def main():
	value1 = int(input("Enter number"))

	ChkEven(value1)

if __name__ == "__main__":
	main()
"""








"""
# Assignment 1.1

def Fun():
	print("Hello from Fun")

def main():
	Fun()

if __name__ == "__main__":
	main()
"""











"""
def main():
	Arr = list()

	print("Please enter how many element you want to store in list")
	size = int(input())

	print("Please enter the values")

	for i in range(0,size):
		no = int(input())
		Arr.append(no)

	print(Arr)

if __name__ == "__main__":
	main()
"""










"""
print("_________________")
value = [10,20,30,40,50]

for i in range(0,len(value),2):
	print(value[i])
print("-----------------")
for no in value:
	print(no)
"""







"""
for i in (range(1,5)):
	print(i)


for i in (range(2,15,2)):
	print(i)
"""




"""
i = 0

while i < 4:
	print("Hello")
	print(i)
	i = i + 1
"""











"""
value = [11,22,33,44,55]
print(value)
print(type(value))
print(len(value))

print(value[3])

value.append(50)
print(value)

value.remove(22)
print(value)
"""




"""
def Maximum(No1, No2):
	if No1 > No2:
		return No1
	else:
		return No2

def main():
	print("----Application of addition program-----")

	Value1 = int(input("Enter the first number :\n"))
	Value2 = int(input("Enter the secound number :\n"))

	result = Maximum(Value1, Value2)
	print("Maximum is : ",result)

if __name__ == "__main__":
	main()
"""







"""
def Addition(No1, No2):
	Ans = No1 + No2
	return Ans

def main():
	print("----Application of addition program-----")

	Value1 = int(input("Enter the first number :\n"))
	Value2 = int(input("Enter the secound number :\n"))

	result = Addition(Value1, Value2)
	print("Addition is : ",result)

if __name__ == "__main__":
	main()

"""








"""
print(__name__)
"""






"""
print("Jay Ganesh...")
"""