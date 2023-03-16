"""
  2 Writer a program which accept number from user and check whether it containcs 0 in it or not.

  Input  : 2395
  Output :	There is no Zero

  Input  : 9000
  Output :	It containcs Zero
"""

def Displayvalue(No):
	digit = 0

	while No != 0:
		digit = No % 10
		if (digit == 0):
			print("It containcs Zero")
			break
		else:
			print("There is no Zero")
			break

def main():
	value = int(input("Enter the numbers"))
	
	Displayvalue(value)

if __name__ == "__main__":
	main()











