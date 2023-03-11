# Accept one number and check whether is divisible by 5 or not.

def Divisible(No):

	for i in range(1,No):
		if No % 5 == 0:
			return True
		else:
			return False

def main():
	print("Please enter the number :")
	Value = int(input())


	BRet = Divisible(Value)

	if (BRet == True):
		print("Divisible by 5")
	else:
		print("Not Divisible by 5")


if __name__ == "__main__":
	main()