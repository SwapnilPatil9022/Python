"""
  1 Writer a program which accept number from user and check whether it containcs reverce number.

  Input  : 2395
  Output : 5
  		   9
  		   3
  		   2
"""

def DisplayRev(No):
	rev_num = 0

	while No != 0:
		digit = No % 10
		rev_num = rev_num * 10 + digit
		No //=10

	print("Reverce number : " + str(rev_num))

def main():
	value = int(input("Enter the numbers"))

	DisplayRev(value)

if __name__ == "__main__":
	main()



"""
num = 123456
print(str(num)[::-1])
"""