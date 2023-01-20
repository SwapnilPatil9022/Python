"""
1. Write a recursive program which display below pattern.
	Input :		5
	Output : 	5	4	3	2	1
"""

def Display(No):
	if(No > 0):
		print(No, end = " ")
		No = No - 1
		Display(No)

def main():
	Value = 5

	Display(Value)

if __name__ == "__main__":
	main()
