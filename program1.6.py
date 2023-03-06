# 6. Write a program which accept number from user and check whether that number is positive or negative or zero.

def Chk(iNo):
    
    if iNo > 0:
        print("Positive number")
    elif iNo < 0:
        print("Negative number") 
    elif iNo == 0:
        print("Zero")  

def main():
    print("Please enter the number :")
    iValue = int(input())
    
    Chk(iValue)

if __name__ == "__main__":
    main()