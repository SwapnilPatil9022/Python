# import Arithmetic           #  OR    
from Arithmetic import *

def main():
    print("Enter the First number")
    iValue1 = int(input())
    
    print("Enter the Secound number")
    iValue2 = int(input())
    
    print("-------------------------")
    
    iRet = Add(iValue1, iValue2)
    print("Addition is :",iRet)
    
    print("-------------------------")
    
    iRet = Sub(iValue1, iValue2)
    print("Substraction is :",iRet)
    
    print("-------------------------")
    
    iRet = Mult(iValue1, iValue2)
    print("Multiplication is :",iRet)
    
    print("-------------------------")
    
    iRet = Div(iValue1, iValue2)
    print("Division is :",iRet)

if __name__ == "__main__":
    main()
    