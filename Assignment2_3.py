# 3. Write a program which accept one number from user and return its factorial.
#	Input : 5			#	Output : 120

def Fact(No):
    factorial = 1
    
    # Check if the number is negative , positive, or zero
    if No < 0:
        print("Sorry, factorial does not exits for negative numbers")
    elif No == 0:
        print("The Factorial of 0 is 1 ")
    else:
        for i in range(1,No+1):
            factorial = factorial * i
        print("Factorial are :",factorial)

def main():
    print("Please enter the value :")
    Value = int(input())
    print("------------------------")
    
    Ret = Fact(Value)

if __name__ == "__main__":
    main()