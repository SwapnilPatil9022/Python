# 2. Write a program which accept N number from user and store it into List. Return Maximum number from that list.
#	input :	 	Number of Elements : 7
#	Input elements : 13   5	  45   7   4   56   34
#	Output :	56

def main():
	Arr = list()

	print("Enter how many elements store in list ?")
	Size = int(input())

	print("Please Enter the elements :")

	for i in range(0,Size):
		no = int(input())
		Arr.append(no)

	Max = 0
	Max = Arr[0]
	for i in range(0,Size):
		if(Arr[i] > Max):
			Max = Arr[i]

	print("Maximum number is :",Max)

if __name__ == "__main__":
	main()