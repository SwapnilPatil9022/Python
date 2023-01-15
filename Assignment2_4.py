# write a program which accept one number from user and return additions of its factors.
#	Input : 12			# Output : 16 (1+2+3+4+6)

def Fact(No):
	Sum = 0

	print("Factors are : ")
	for i in range(1,No):
		if No % i == 0:
			Sum = Sum + i
			print(i)
	print("-----------------")
	print(Sum)
			

def main():
	print("Please Enter the number :")
	Value = int(input())

	Fact(Value)

if __name__ == "__main__":
	main()