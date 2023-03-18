# Accept one number from user if number is less than 10 then print "Hello" otherwise print "Demo".

def Display(No):

	size = 10

	for i in range(1,No+1):
		if(size > No):
			print("Hello")
		else:
			print("Demo")

		
def main():
	print("Please enter the number :")
	Value = int(input())

	Display(Value)

if __name__ == "__main__":
	main()