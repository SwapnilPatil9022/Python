# Accept one number from user and print that number of * on screen using while loop

def Display(No):

	i = 1

	while(i < No+1):
		i = i + 1
		print("*", end = " ")
		
def main():
	print("Please enter the number :")
	Value = int(input())

	Display(Value)

if __name__ == "__main__":
	main()