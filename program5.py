# Accept one number from user and print that number of * on screen

def Display(No):

	for i in range(1,No+1):
		print("*", end = " ")
		
def main():
	print("Please enter the number :")
	Value = int(input())

	Display(Value)

if __name__ == "__main__":
	main()