"""
  3 Writer a program which accept number from user and return count of digits in between 3 and 7.

  Input  : 2395
  Output :	1

  Input  : 1018
  Output :	0
"""

def Count(No):
	cnt = 0

	while (No != 0):
		digit = No % 10
		if digit > 3 and digit < 7:
			cnt = cnt + 1
		No = No // 10
	print(cnt)

def main():
	value = int(input("Enter the numbers : "))
	
	Count(value)

if __name__ == "__main__":
	main()

