"""
  3 Writer a program which accept number from user and count frequency of 2 in it.

  Input  : 2395
  Output :	1

  Input  : 9000
  Output :	0
"""

def Display(No,Search):
	cnt = 0

	while (No):
		digit = No % 10
		if digit == Search:
			cnt = cnt + 1
		No = No // 10
	print(cnt)

def main():
	value = int(input("Enter the numbers"))
	find_num = int(input("Enter the number that you want to find :"))
	
	Display(value,find_num)

if __name__ == "__main__":
	main()











