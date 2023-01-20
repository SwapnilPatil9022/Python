"""
1. Write a recursive program which Accept number from user and return its factorial.
	Input :		5
	Output : 	120
"""
fact = 1

def Displayfactorial(No):
		global fact
		if(No != 0):
			fact = fact * No
			No = No - 1
			Displayfactorial(No)
			return fact

def main():
	print("Enter number :")
	No = int(input())

	Ret = Displayfactorial(No)
	print("factorial are : ",Ret)

if __name__ == "__main__":
	main()
