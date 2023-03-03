	
def Add(No):
	if(No <= 0):
		return 0
	else:
		return (No + Add(No-1))
		
Ret = Add(4)
print("Result is : ",Ret)


"""
def Display(No):
	if(No > 0):
		No = No - 1
		Display(No)
		print(No)

Display(4)
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

	if (Cnt < No):
		print("Hello")
		Cnt = Cnt + 1
		Display(No)

Display(4)
"""


"""
def substraction(No1,No2):
	Ans = 0
	Ans = No1 - No2
	return Ans

def Decorated_Function(Function_Name):
	def Inner(A,B):
		if(A < B):
			A,B = B,A	
		Output = Function_Name(A,B)		
		return Output
	return Inner

def main():
	Value1 = int(input("Enter first number :"))
	Value2 = int(input("Enter secound number : "))

	New_Function = Decorated_Function(substraction)
	print(New_Function(Value1,Value2))

if __name__ == "__main__":
	main()
"""

"""
def Outer():
	print(id(Outer))
	print("Inside outer : ")

	def Inner():
		print("Inside Inner : ")

	print(id(Inner))
	return Inner

ret = Outer()
print(type(ret))
print(id(ret))
ret()
"""


"""

def Add(A,B):
	return A+B

def Sub(A,B):
	return A-B

def Calculater(Target, Value1, Value2):
	return Target(Value1, Value2)

Ret = Calculater(Target = Add,Value1 = 10, Value2 = 11)
print("addition is : ",Ret)

Ret = Calculater(Target = Sub,Value1 = 10, Value2 = 11)
print("Substraction is : ",Ret)
"""


"""
def Demo():
	print("Inside Hello")

def Fun():
	print("Inside fun")

def Hello(FPTR):
	print("Inside Demo")
	FPTR()

Hello(Demo)
Hello(Fun)

"""





"""
def main():
	print("Enter frist number : ")
	No1 = int(input())

	No2 = int(input("Enter secound number : "))

	try:
		Ans = No1 / No2
		print("Division is : ",Ans)

	except ZeroDivisionError:
		print("Exception occuerd : ")

	except ValueError:
		print("value is  occuerd : ")

	except Exception:
		print("value is  occuerd : ")

	finally:
		print("inside finaly block : ")

if __name__ == "__main__":
	main()
"""


"""
import threading 
import multiprocessing
import time

def DisplayEven(No):
	for i in range(1,No+1):
		if(i % 2 == 0):
			print("Even number : ",i)

def DisplayOdd(No):
	for i in range(1,No+1):
		if(i % 2 != 0):
			print("Odd number : ",i)

def main():
	print("Demonstration of multiprocessing ; ")
	Number = 2000000
	
	P1 = threading.Thread(target = DisplayEven, args = (Number,))
	P2 = threading.Thread(target = DisplayOdd, args = (Number,))

	p1 = multiprocessing.Process(target = DisplayEven, args = (Number,))
	p2 = multiprocessing.Process(target = DisplayEven, args = (Number,))

	p1.start()
	p2.start()

	p1.join()
	p2.join()

	P1.start()
	P2.start()

	P1.join()
	P2.join()
	print("ENd of main :")

if __name__ == "__main__":
	start_time = time.process_time()
	main()
	end_time = time.process_time()
	print("Execution time is : ",end_time - start_time)
"""


"""

import multiprocessing
import time

def DisplayEven(No):
	for i in range(1,No+1):
		if(i % 2 == 0):
			print("Even nember : ",i)

def DisplayOdd(No):
	for i in range(1,No+1):
		if(i % 2 != 0):
			print("Odd nember : ",i)

def main():
	print("Demonstration of multiprocessing ; ")
	Number = 20000
	
	p1 = multiprocessing.Process(target = DisplayEven, args = (Number,))
	p2 = multiprocessing.Process(target = DisplayOdd, args = (Number,))

	p1.start()
	p2.start()

	p1.join()
	p2.join()
	print("ENd of main :")

if __name__ == "__main__":
	start_time = time.process_time()
	main()
	end_time = time.process_time()
	print("Execution time is : ",end_time - start_time)

"""




"""



def DisplayEven(No):
	for i in range(1,No):
		if(i % 2 == 0):
			print("Even nember : ",i)

def DisplayOdd(No):
	for i in range(1,No):
		if(i % 2 != 0):
			print("Odd nember : ",i)

def main():

	DisplayEven(20)
	DisplayOdd(20)


if __name__ == "__main__":
	main()

"""