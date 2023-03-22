# Write a program which accept one number from user and print that number of even factors on that numbers.
#	Input : 24
# 	Output : 1	2	4	6	8	12

def DisplayFact(No):

	if(No < 0):
		No = -No
		
	for i in range(1,No):
		if (No % i == 0):
			print(i)


def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayFact(Value)

if __name__ == "__main__":
	main()