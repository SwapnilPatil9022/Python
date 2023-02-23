
class Value:

	def __init__(self,Data):
		self.No = Data

	def SumFactors(self):
		Sum = 0
		for i in range(1,int(self.No/2)+1):
			if(self.No % i == 0):
				Sum = Sum + i

		return Sum

	def ChkPerfect(self):
		Ans = self.SumFactors()

		if(self.No == Ans):
			return True
		else:
			return False

	def ChkPrime(self):
		i = 0

		for i in range(2,int(self.No / 2)+1):
			if(self.No % i == 0):
				break

			if(i == int(self.No/2)):
				return True
			else:
				return False

def main():
	print("enter number : ")
	A = int(input())

	Obj = Value(A)

	Ret = Obj.ChkPrime()
	if(Ret == True):
		print("{} is a prime number".format(A))
	else:
		print("{} is a not a prime numebr".format(A))

if __name__ == "__main__":
	main()


"""



class Arithematic:

	def __init__(self):
		self.Size = 0
		self.Arr = list()

	def Accept(self):
		print("Enter how many element you wnat to store in list : ")
		self.Size = int(input())

		print("Enter the element : ")
		Value = 0
		for i in range(0,self.Size):
			Value = int(input())
			self.Arr.append(Value)

	def Display(self):
		print("Element from list is : ")
		for i in range(0,self.Size):
			print(self.Arr[i])

	def Summation(self):
		Sum = 0
		for i in range(0,self.Size):
			Sum = Sum + self.Arr[i]
			
		return Sum

	def Average(self):
		Sum = 0
		for i in range(0,self.Size):
			Sum = Sum + self.Arr[i]
			
		return (Sum/self.Size)

	def Maximun(self):
		Max = self.Arr[0]		
		for i in range(0,self.Size):
			if (self.Arr[i] > Max):
				Max = self.Arr[i]
			
		return Max

	def Minimun(self):
		Min = self.Arr[0]		
		for i in range(0,self.Size):
			if (self.Arr[i] < Min):
				Min = self.Arr[i]
			
		return Min

def main():
	Obj = Arithematic()

	Obj.Accept()
	Obj.Display()

	Output = Obj.Summation()
	print("Summation is : ",Output)

	Output = Obj.Average()
	print("Summation is : ",Output)

	Output = Obj.Maximun()
	print("Maximun is : ",Output)

	Output = Obj.Minimum()
	print("minimum is : ",Output)

if __name__ == "__main__":
	main()









"""



















#from functools import reduce
"""
def ChkEven(No):
	return (No % 2 == 0)

def Double(No):
	return No*2

def Sum(A,B):
	return A+B
"""
"""

def main():
	print("Enter the element that you want to store in list : ")
	iSize = int(input())

	Data_Input = []
	print("Enter the element : ")
	for i in range(0,iSize):
		Value = int(input())
		Data_Input.append(Value)

	print(Data_Input)

	Data_reduce = reduce(lambda A,B : A+B ((map(lambda No : No * 2)(filter(lambda No : No % 2 == 0)))))
	#Data_reduce = filter(map(reduce(lambda A,B : A+B (lambda No : No * 2 (lambda No : No % 2 == 0)))))
	print("data after reduce : ",Data_reduce)

if __name__ == "__main__":
	main()
"""
"""
	Data_filter = list(filter(lambda No : No % 2 == 0,Data_Input))
	print("Data after filter is : ",Data_filter)

	Data_Map = list(map(lambda No : No * 2,Data_filter))
	print("Data after maping : ",Data_Map)

	Data_reduce = reduce(lambda A,B : A+B,Data_Map)
	print("data after reduce : ",Data_reduce)
"""