# 3. Write a program which accept N number from user and store it into List. Return Minimum number from that list.
#	input :	 	Number of Elements : 4
#	Input elements : 13   5	  45   7  
#	Output :	5

def main():
	Arr = list()

	print("Enter how many element store in the list ?")
	Size = int(input())

	print("Please enter the elements :")

	for i in range(0,Size):
		no = int(input())	
		Arr.append(no)

	Min = 0
	Min = Arr[i]
	for i in range(0,Size):
		if(Arr[i] < Min):
			Min = Arr[i]

	print("Minimum number is :",Min)

if __name__ == "__main__":
	main()