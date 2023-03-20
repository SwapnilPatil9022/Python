# Accept one number from user if number and display first number in secound number of times.
#	Input : 12	5
#	Output : 12  12	 12	 12	 12

def Display(No1,No2):

	for i in range(1,No2+1):
		print(No1, end = " ")

		
def main():
	print("Please enter first number :")
	Value1 = int(input())

	print("How Many times display the number :")
	Value2 = int(input())

	Display(Value1,Value2)

if __name__ == "__main__":
	main()