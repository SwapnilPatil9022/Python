# 3. Write a program which contains one function named as Add() which acceptes two numbers from user and return addition of that two numbers.

def Add(iNo1, iNo2):
    
    Ans = iNo1 + iNo2
    
    return Ans

def main():
    
    print("Enter the First number.")
    iValue1 = int(input())
    
    print("Enter the Secound number.")
    iValue2 = int(input())
    
    iRet = Add(iValue1, iValue2)
    print("------------------------------")
    print("Addition is :",iRet)

if __name__ == "__main__":
    main()