# programs to divide two numbers

def Divide(A,B):
	Ans = A / B
	return Ans

def main():
	print("Enter First Number :")
	No1 = int(input())

	print("Enter Secound number :")
	No2 = int(input())

	Ret = Divide(No1,No2)
	print("Divided number is :",Ret)

if __name__ == "__main__":
	main()