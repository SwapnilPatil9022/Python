"""
  4 Writer a program which accept number from user and return Multiplication of all digits.

  Input  : 2395
  Output :	270

  Input  : 1018
  Output :	8
"""

def CountMult(No):
	mult = 1
	digit = 0

	while (No != 0):
		digit = No % 10
		if (digit == 0):
			digit = 1
		mult = mult * digit
		print(mult)
		No = No // 10
	print("-----------")
	print(mult)
	
def main():
	value = int(input("Enter the numbers : "))
	
	CountMult(value)

if __name__ == "__main__":
	main()

