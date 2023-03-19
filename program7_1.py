"""
  1 Writer a program which accept number from user and return count of even digits.

  Input  : 2395
  Output :	1

  Input  : 8462
  Output :	4
"""

def CountEven(No):
	cnt = 0

	while (No != 0):
		digit = No % 10
		if digit % 2 == 0:
			cnt = cnt + 1
		No = No // 10
	print(cnt)

def main():
	value = int(input("Enter the numbers : "))
	
	CountEven(value)

if __name__ == "__main__":
	main()

