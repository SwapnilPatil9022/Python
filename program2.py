# program to print 5 times Marvellous on screean

def Display():

	print("Enter how many times display the world :")
	no = int(input())
	
	str = "Marvellous"

	for i in range(0,no):
		print(str)

def main():

	Display()

if __name__ == "__main__":
	main()