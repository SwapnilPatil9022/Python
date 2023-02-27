def Double(No):
	erturn (NO*2)

def CheckEven(No):
    return (No >= 70 and No <= 90)
    
def filterX(Helper_Function, Data):
    Result = []
    for No in Data:
        if(Helper_Function(No) == True):
            Result.append(No)
    return Result

def mapX(Helper_Function, Data):
	Result = []
	for No in Data:
		Value = Helper_Function(No)
		Result.append(Value)
    
def main():
    print("Enter number of elements you want to enter :")
    iSize = int(input())
   
    Data_Input = []
    print("Please enter the data :")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
        
    print("Data is :",Data_Input)
    
    Data_Filter = filterX(CheckEven, Data_Input)
    
    print("Data after filter is :",Data_Filter)

    Data_Map = mapX(Double,Data_Map)
    print("Data after map is :",Data_Map)
    
if __name__ == "__main__":
    main()





"""

def CheckEven(No):
    return (No % 2 == 0)
    
def filterX(Helper_Function, Data):
    Result = []
    for No in Data:
        if(Helper_Function(No) == True):
            Result.append(No)
    return Result
    
def main():
    print("Enter number of elements you want to enter :")
    iSize = int(input())
   
    Data_Input = []
    print("Please enter the data :")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
        
    print("Data is :",Data_Input)
    
    Data_Filter = filterX(CheckEven, Data_Input)
    
    print("Data after filter is :",Data_Filter)
    
if __name__ == "__main__":
    main()
"""

"""

def main():
	Arr = list()
	prime = []

	print("Enter how many element store in the list ?")
	Size = int(input())

	print("Please enter the elements :")

	C = 0

	for i in range(0,Size):
		no = int(input())	
		Arr.append(no)
	print(Arr)

	if i % no == 0:
		C = C + i
		Arr.append(no)
	print(Arr)



if __name__ == "__main__":
	main()
"""








"""
def main():
	Arr = list()

	print("Enter how many element store in the list ?")
	Size = int(input())

	print("Please enter the elements :")

	for i in range(0,Size):
		no = int(input())	
		Arr.append(no)

	print("Please o search :")

	freq = 0

	for i in range(2,int(no / 2) + 1):
        if(No % i == 0):
			freq = freq + 1

	if freq == 0:
		print(search,"has not been found in the list.!!")
	else:
		print(search," has frequency as",freq,"in the list,")

if __name__ == "__main__":
	main()
"""



"""

def filterX(Arr):
	Result = []
	FN = 0
    
    for no in Arr:
        if(FN(no)):
            Result.append(no)
    return Result

def mapX(Arr,Function_Name):
    Result = []
    for no in Arr:
        value = Function_Name(no)
        Result.append(value)
    return Result

def reduceX(Arr):
    Sum = 0
    for no in Arr:
        Sum = Sum + no
    return Sum

def main():
    Data = [13,3,45,7,4,56,10,34,2,5,8]
    print("Original data : ",Data)

    Data_Filter = list(filterX(Data,No))
    print("Data after filter : ",Data_Filter)

    Data_map = list(mapX(Data_Filter,Increment))
    print("Data after map : ",Data_map)

    Ret = reduceX(Data_map)
    print("Data after reduce : ",Ret)

if __name__ == "__main__":
    main()

"""

"""
class Value:

    def __init__(self,Data):
        self.No = Data

    def CheckPrime(self):
        i = 0

        for i in range(2,int(self.No / 2) + 1):
            if(self.No % i == 0):
                break
        
        if(i == int(self.No/2)):
            return True
        else:
            return False
            
def main():
	Data = list()

	print("Enter how many element you want to store in list :")
	size = int(input())

	print("please enter the values")

	for i in range(0,size):
		no = int(input())
		Data.append(no)
	print(Data)

    obj = Data()

    Ret = obj.CheckPrime()
    if(Ret == True):
        print("{} is a prime number".format(A))
    else:
        print("{} is not a prime number".format(A))


if __name__ == "__main__":
    main()
"""

"""
def Increment(No):
	return No+2

def filterX(Arr,Function_Name):
	Result = []
	for no in Arr:
		if(Function_Name(no)):
			Result.append(no)
	return Result

def mapX(Arr,Function_Name):
	Result = []
	for no in Arr:
		value = Function_Name(no)
		Result.append(value)
	return Result

def Summation(Arr):
	Sum = 0
	for no in Arr:
		Sum = Sum + no
	return Sum

def main():
	Data = list()

	print("Enter how many element you want to store in list :")
	size = int(input())

	print("please enter the values")

	for i in range(0,size):
		no = int(input())
		Data.append(no)
	print(Data)

	Data_eFilter = list(filterX(Data,size))

	print("Data after filter :",Data_Filter)

	Data_map = list(mapX(Data_Filter,Incremnt))

	print("Data after map :",Data_map)

	Ret = Summation(Data_map)

	print("Data after reduce :",Ret)

if __name__ == "__main__":
	main()
"""


"""
def CheckEven(No):
	if (No % 2 == 0):
		return True
	else:
		return False

Even = lambda No : No % 2 == 0

def main():
	Ret = Even(12 )

	if (Ret == True):
		print("Its even")
	else:
		print("Its odd")


if __name__ == "__main__":
	main()
"""


"""
def Add(No1,No2):
	return No1+No2

AddFunction = lambda A,B : A + B

def main():
	Ans1 = Add(10,11)
	print(Ans1)
	Ans2 = AddFunction(10,11)
	print(Ans2)

if __name__ == "__main__":
	main()

"""




"""
def Add(*Value):
	print(type(Value))
	print("Number of argumnt are :",len(Value))

	Sum = 0

	for no in Value:
		Sum = Sum + no

	return Sum


def AddX(*Value):
	print(type(Value))
	print("Number of argumnt are :",len(Value))

	for i in range(0,len(Value)):
		Sum = 0
		Sum = Sum + Value[i]

	return Sum

def main():
	Ans = Add(1,7,9,4,6,5)
	print("Additon  is :",Ans)

if __name__ == "__main__":
	main()
"""


"""
def Area(Redius, PI = 3.14):
	Result = PI * Redius
	return Result

def main():
	RValue = 10.5
	PIValue = 3.14

	Ans = Area(RValue,PIValue)
	print("Area of circle is :",Ans)

	Ans = Area(PI = PIValue, Redius = RValue)
	print("Area of circle is :",Ans)	

	Ans = Area(PI = 7.10, Redius = 10.5)
	print("Area is :",Ans)

	Ans = Area(10.5)
	print("Area is :",Ans)

if __name__ == "__main__":
	main() 

"""


"""
def Add1(No1,No2):
	print("Value of No1 : ",No1)
	print("Vlaue of No2 : ",No2)
	return No1 + No2

def Sub1(No1,No2):
	print("Value of No1 : ",No1)
	print("Vlaue of No2 : ",No2)
	return No1 - No2

def main():

	Ans = Add1(10,11)
	print("Addition is :",Ans)

	Ans = Sub1(No2 = 10, No1 = 11)
	print("substracton is :",Ans)

	Ans = Sub1(No1 = 10, No2 = 11)
	print("substracton is :",Ans)



if __name__ == "__main__":
	main()
"""


"""
def Demo1():
	print("Inside Demo1")	


def Demo2(No):
	print("Inside Demo2",No)
	print("--------------")

def Demo3(No):
	print("Inside Demo3",No)
	return No+2
	print("--------------")

def Demo4(No1,No2):
	print("Inside Demo4",)
	Add = No1 + No2
	return Add
	print("--------------")

def Demo5(No1,No2):
	print("Inside Demo5",)
	Add = No1 + No2
	Sub = No1 - No2
	Mult = No1 * No2
	Div = No1 / No2
	return Add,Sub,Mult,Div
	print("--------------")

def main():
	Demo1()
	Demo2("Hello")
	Ret = Demo3(10)
	print("Retuen value of Demo3 is :",Ret)
	print("--------------------------")

	Ret = Demo4(11,21)
	print("Retuen value of Demo3 is :",Ret)
	print("--------------------------")

	Ans1,Ans2,Ans3,Ans4 = Demo5(11,10)
	print("First return value is :",Ans1)
	print("Secound return value is :",Ans2)
	print("Third return value is :",Ans3)
	print("Four return value is :",Ans4)


if __name__ == "__main__":
	main()

"""

"""
programming = {"C" : "Riche", "C++" : "Strounstrup", "java" : "Gosling", "Python" : "Rossum"}
Baches = {"PPA" : 10000, "LB" : 16700, "Python" : 16500, "Anguler" : 15000}

print("Data : ",Baches)
print("Data type : ",type(Baches))
print("Length of Document :", len(Baches))
print("value PPA :",Baches["PPA"])

for x in Baches:
	print(x, Baches.get(x))

keyBaches = Baches.keys()
print(keyBaches)

valueBaches = Baches.values()
print(valueBaches)

for i in range(0,len(Baches)):
	print("B name :",keyBaches[i])
	print("Fees : ",valueBaches[i])

	"""


"""
data = {11,21,51,101,21,11}
data1 = {11, 90.80, True, "HEllo"}

print("------------")

for i in data:
	print(i, end = " ")

print("------------")

"""


"""
data = {11,21,51,101,21,11}
data1 = {11, 90.80, True, "HEllo"}

print("Hetrogenenous :",data)
print("Orderd :",data)
#print("index :",data(2))
print("duplicate :",data)
print("-------------------")
print("Hetrogenenous :",data1)
print("Orderd :",data1)
#print("index :",data1[2])
print("duplicate :",data1)
print("-----------------")

print(type(data))
data.add(500)
print(data)

print("-----------------")

data.remove(500)
print(data)
"""


"""
print("------------")

for no in Data:
	print(no, end = " ")

print("------------")

for i in range(0,len(Data)):
	print(Data[i], end = " ")

print("------------")

i = 0

while(i < len(Data)):
	print(Data[i], end = " ")
	i = i + 1
"""


"""
data = (11,21,51,101,21,11)
data1 = (11, 90.80, True, "HEllo")

print("Hetrogenenous :",data)
print("Orderd :",data)
print("index :",data[2])
print("duplicate :",data)
print("-------------------")
print("Hetrogenenous :",data1)
print("Orderd :",data1)
print("index :",data1[2])
print("duplicate :",data1)
print("-----------------")

print(type(data))
print("-----------------")
data.pop()
print(data)

print("-----------------")
data1.append(500)
print(data1)
print(type(data1))
print("-----------------")
data1.pop()
print(data1)

"""




"""
data = [11,21,51,101,21,11]
data1 = [11, 90.80, True, "HEllo"]

print("Hetrogenenous :",data)
print("Orderd :",data)
print("index :",data[2])
print("duplicate :",data)
print("-------------------")
print("Hetrogenenous :",data1)
print("Orderd :",data1)
print("index :",data1[2])
print("duplicate :",data1)
print("-----------------")
data.append(500)
print(data)

print("-----------------")
data.pop()
print(data)

print("-----------------")
data1.append(500)
print(data1)

print("-----------------")
data1.pop()
print(data1)
"""



"""
x = (("Apple", "Cherry", "Banana"))

print(x)
print(type(x))
"""


"""

from sys import*

def Addition(A,B):
	Ans = 0
	Ans = A + B
	return Ans

def main():
	print("Welcome to :",argv[0])

	if(argv[1] == "--U"):
		print("use the application as :")
		print("Python_name_of_application First_number secound_number")
		exit()

	if(argv[1] == "--H"):
		print(" this file use the Addition perfrom")
		exit()

	if(len(argv) != 3):
		print("Invalid number of arguments")
		print("please use --U ar --u flag for the usage")
		exit()

	Ret = Addition(int(argv[1]), int(argv[2]))

	print("Addition is :",argv[1]," + ", argv[2]," = ",Ret)

	print("Thanku for the using applications")
	print("Learning Phase by Swapnil Ashok Patil")


if __name__ == "__main__":
	main()

"""


"""
from sys import*

def Addition(A,B):
	Ans = 0
	Ans = A + B
	return Ans

def main():
	if(len(argv) != 3):
		print("Invalid number of argument")
		exit()

	Ret = Addition(int(argv[1]), int(argv[2]))
	print("Addition is : ",Ret)


if __name__ == "__main__":
	main()
"""

"""
from sys import*

def main():
	print("total number of argument are :",len(argv))

	print("Name of application",argv[0])

	print("first argument",argv[1])
	print("Secound argument",argv[2])
	print("Third argument",argv[3])

if __name__ == "__main__":
	main()
"""



"""
from p2 import DisplayF
from sys import *

def main():
    DisplayF(int(argv[1]))

if __name__ == "__main__":
	main()
"""

"""
#from p2 import *
#import p2
#import p2 as p
from p2 import DisplayF

def main():
	print("Enter number")
	no = int(input())

	DisplayF(no)
	
if __name__ == "__main__":
	main()
"""


"""
def main():
	print("Enter number")
	no = int(input())

	print("Factors are :")

	i = 1

	while(i <= int(no/2)+1):
		if no % i == 0:
			print(i)
		i = i + 1
	
if __name__ == "__main__":
	main()
	"""




"""
def main():
	print("Enter number")
	no = int(input())

	print("Factors are :")

	for i in range(1,int(no//2)+1):
		if no % i == 0:
			print(i)

if __name__ == "__main__":
	main()
"""


"""

def main():
	print("Enter number")
	no = int(input())

	print("Factors are :")

	for i in range(1,no):
		if no % i == 0:
			print(i)
		i = i + 1

if __name__ == "__main__":
	main()
"""



"""
def main():
	Arr = "*"

	print("Enter how many elements that you want to store in your list")
	size = int(input())

	print("Please enter the elements")
	
	for i in range(1,size):
		for j in range(1,size):
			if i == j:
				print("*", end = " ")

	print(Arr)

if __name__ == "__main__":
	main()
"""

"""
def main():
	Arr = list()

	print("Enter how many elements that you want to store in your list")
	size = int(input())

	print("Please enter the elements")
	
	for i in range(0,size):
		no = int(input())
		Arr.append(no)

	print(Arr)

if __name__ == "__main__":
	main()
"""



"""
value1 = [10,20,30,40,50]

print(value1[0])
print(value1[1])
print(value1[2])
print(value1[3])
print(value1[4])

for i in range(0,len(value1)):
	print([i])

print("--------------------------")

for no in value1:
	print(no)

"""




"""
no = "Hello"

for i in range(0,5):
	print(no)
"""

"""
i = 0

while i < 4:
	print("World")
	i = i + 1
	print(i)

"""


"""
value1 = [10,20,30,40,50]
value2 = (10,20,30,40,50)
value3 = {10,20,30,40,50}
value4 = {"A" : 100, "B" : 200}

value1.reverse()
print(value1)

print(type(value1))
print(type(value2))
print(type(value3))
print(type(value4))

print(len(value1))
print(len(value2))
print(len(value3))
print(len(value4))

print(value1[0])
print(value1)

value1.append(60)
value1.append(60.90)
print(value1)

value1.remove(60)
print(value1)

value1.insert(2,11)
value1.insert(10,111)

print(value1)

value1.reverse()
print(value1)
"""

"""
def Maximum(No1,No2):
	if No1 > No2:
		return No1
	else:
		return No2

def main():
	print("Enter First number :")
	Value1 = int(input())

	print("Enter secound number")
	Value2 = int(input())

	Ans = Maximum(Value1,Value2) 
	print("Largest number is :",Ans)

if __name__ == "__main__":
	main()

	"""