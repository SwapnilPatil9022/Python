# Accept one number from user and check whether number is even or odd.

def ChkEvenOdd(No1):

	for i in range(1,No1+1):
		if (No1 % 2) == 0:
			print("Even number")
			exit()
		else:
			print("Odd numebr")
			exit()

		
def main():
	print("Please enter number :")
	Value1 = int(input())

	ChkEvenOdd(Value1)

if __name__ == "__main__":
	main()