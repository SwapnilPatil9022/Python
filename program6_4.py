"""
  4 Writer a program which accept number from user and count frequency of 4 in it.

  Input  : 2395
  Output :	0

  Input  : 9440
  Output :	2
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
	value = int(input("Enter the numbers : "))
	find_num = 4
	
	Display(value,find_num)

if __name__ == "__main__":
	main()











