# 8. Write a program which accept one number and display below pattern.
"""
	Input : 5

	Output : 1
			 1	2
			 1	2	3
			 1	2	3	4
			 1	2	3	4	5
"""

def Pattern(No):

	for i in range(1,No+1):
		for j in range(1,No+1):
			if i >= j:
				print(i, end = " ")
		print()

def main():
	print("Please enter the number")
	Value = int(input())

	Pattern(Value)

if __name__ == "__main__":
	main()

