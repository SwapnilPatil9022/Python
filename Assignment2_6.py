# 6. Write a program which accept one number and display below pattern.
"""
	Input : 5

	Output : 	*	*	*	*	*
				*	*	*	*
				*	*	*
				*	*
				*
"""

def Display(No):

	for i in range(0,No+1):
		for j in range(0,No+1):
			if i < j:
		 		print("*\t",end = " ")
		print()

def main():
	print("Please enter the value :")
	Value = int(input())

	Display(Value)

if __name__ == "__main__":
	main()