"""
def main():
    A = 10;
    B = 20;
    C = 0;
    
    C = A + B;
    print("Additon is :",C)
"""
def  Addition(iNo1, iNo2):
    iRet = iNo1 + iNo2
    
    return iRet
        
def main():
    print("Enter First number")
    iValue1 = input()
    
    print("Enter Secound number")
    iValue2 = input()
    
    Ans = Addition(int(iValue1), int(iValue2))
    
    print("Addition is :",Ans)
    
if __name__ == "__main__":
    main()