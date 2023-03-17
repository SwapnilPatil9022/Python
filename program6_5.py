"""
  5 Writer a program which accept number from user and count frequency of such a digits which are less than 6.

  Input  : 2395
  Output :	3

  Input  : 96672
  Output :	1
"""

def Display(No,Search):
	cnt = 0

	while (No != 0):
		digit = No % 10
		if digit < Search:
			cnt = cnt + 1
		No = No // 10
	print(cnt)

def main():
	value = int(input("Enter the numbers : "))
	num = 6
	
	Display(value,num)

if __name__ == "__main__":
	main()

