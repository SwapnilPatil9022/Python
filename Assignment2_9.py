# 9. Write a program which accept number from user and return number of digits in that number.
# 		Input : 5187934				# Output : 7

def Digit(No):
	i = 0

	if No < 0:
		No = -1 * No
	if No == 0:
		i = 1
	while No != 0:
		No = No // 10
		i = i + 1

	print("Number of digits are :",i)

def main():
	print("Please enter the numbers")
	Value = int(input())

	Digit(Value)

if __name__ == "__main__":
	main()
