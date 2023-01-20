"""
1. Write a recursive program which display below pattern.
	Input :		5
	Output : 	*	*	*	*	*
"""

def Pattern(i):
	if(i < 5):
		print(" * ", end = " ")
		i = i + 1
		Pattern(i)

def main():
	Value = 0

	Pattern(Value)

if __name__ == "__main__":
	main()
