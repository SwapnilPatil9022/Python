# 5. Write a program which accept one number from user and check whether number is prime or not.

def Prime(No):
    
    for i in range(1,No):
        if No % i  == 0:
            print("prime number")
            break
    else:
        print("It is not a prime number")
    
def main():
	print("Please enter the value :")
	Value = int(input())

	Prime(Value) 

if __name__ == "__main__":
	main()