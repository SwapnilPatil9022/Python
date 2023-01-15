# 1. Write a program which accept N number from user and store it into List. Return addition of all elements from that list.
#	input :	 	Number of Elements : 6
#	Input elements : 13   5	  45   7   4   56
#	Output :	130 

def main():
	Arr = list()

	print("How many number of elements that you want to store in list ?")
	size = int(input())

	print("Please enter the elements :")

	Cnt = 0

	for i in range(0,size):
		no = int(input())
		Arr.append(no)
		Cnt = Cnt + Arr[i]

	print(Arr)
	print("Addition of all elements is :",Cnt)

if __name__ == "__main__":
	main()
