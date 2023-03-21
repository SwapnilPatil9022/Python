# Write a program which accept one number from user and print that number of even numbers on screen.
#	Input : 7
# 	Output : 2	4	6	8	10	12	14

def DisplayNum(No):

	for i in range(0,No*2):
		i = i + 1
		if (i % 2)== 0:
			print(i)


def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayNum(Value)

if __name__ == "__main__":
	main()