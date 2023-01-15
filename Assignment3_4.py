# 4. Write a program which accept N number from user and store it into List. Accept one another number from user and return frequency of that number from list.
#	input :	 	Number of Elements : 11
#	Input elements : 13   5	  45   7   4   56   5   34   2   5   65
#	Element of search :	5
#	Output : 	3


def main():
	Arr = list()

	print("Enter how many element store in the list ?")
	Size = int(input())

	print("Please enter the elements :")

	for i in range(0,Size):
		no = int(input())	
		Arr.append(no)

	print("Please enter the number that you want to search :")
	search = int(input())

	freq = 0

	for i in range(0,Size):
		if search == Arr[i]:
			freq = freq + 1

	if freq == 0:
		print(search,"has not been found in the list.!!")
	else:
		print(search," has frequency as",freq,"in the list,")

if __name__ == "__main__":
	main()

