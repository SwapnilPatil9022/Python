# 10. Write a program Which accept number from user and return Addition of digits in that number.
#	Input : 5187934			Output : 37

def Digit(No):
	sum = 0

	while(No > 0):
		sum = sum+No%10
		No = No // 10
	print("Sum of digits are :",sum)


def main():
	print("Please enter the number :")
	Value = int(input())
	print("-------------------------")

	Digit(Value)

if __name__ == "__main__":
	main()