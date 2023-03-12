"""
 4.4 Writer a program which accept number from user and display summation of all non factors.

 	Input : 12
 	Output : 50

	Input  : 10
	Output : 37
"""
def DisplayNonFact(No):

	cnt = 0
	
	for i in range(1,No+1):
		if No % i != 0:
			print(i ,"+", end = " ")
			cnt = cnt + i
	print("\n")
	print("summation of all non factors : ",cnt)
	
def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayNonFact(Value)

if __name__ == "__main__":
	main()

