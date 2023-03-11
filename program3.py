# program to print 5 to 1 numbers on screen.

def Display(no):

	for i in range(no+1,1,-1):
		i = i - 1
		print(i, end = " ")

def main():
	print("Please enter the elements :")
	Value = int(input())

	Display(Value)	

if __name__ == "__main__":
	main()
