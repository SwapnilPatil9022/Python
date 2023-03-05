# 2. Write a program which containce one function named as ChkNum() which accept one parameter as number. If number is even then it should display "Even number" otherwise display "Odd number" on console.

def ChkNum(iNo):
    if(iNo % 2) == 0:
        print("Even number...")
    else:
        print("Odd number...")
        
        return iNo

def main():
    print("Please enter the number...")
    iValue = int(input())
    
    iRet = ChkNum(iValue)

if __name__ == "__main__":
    main()
    