# 8. Write a program which accept number from user and print that number of "*" on screen.
#   Input : 5           Output : *   *   *   *   *

def Display(iNo):
    iCnt = 0
    
    for i in range(0,iNo):
        print("*",end="  ")
        iCnt = iCnt + 1
        
    
def main():
    print("Please Enter the number :")
    iValue = int(input())
   
    Display(iValue)
    
if __name__ == "__main__":
    main()