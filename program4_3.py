"""
 4.3 Writer a program which accept number from user and display all non factors.

 	Input : 12
 	Output : 5	7	8	9	10	11 

	Input  : 10
	Output : 3	4	6	7	8	9
"""
def DisplayNonFact(No):
	
	for i in range(1,No+1):
		if No % i != 0:
			print(i, end = " ")
	
def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayNonFact(Value)

if __name__ == "__main__":
	main()
