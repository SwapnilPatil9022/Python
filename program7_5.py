"""
  5 Writer a program which accept number from user and return difference between summation of even digit and odd digit.

  Input  : 2395
  Output :	-15 (2 - 17)

  Input  : 1018
  Output :	6 (8 - 2)
"""

def CountDiff(No):
	Even = 0
	Odd = 0

	while (No != 0):
		digit = No % 10
		if (digit % 2 == 0):
			Even = Even + digit
		elif (digit % 2 != 0):
			Odd = Odd + digit
		No = No // 10
	
	print(Even - Odd)

def main():
	value = int(input("Enter the numbers : "))
	
	CountDiff(value)

if __name__ == "__main__":
	main()

