from Numbers import *                      
from sys import *

def Addition(A,B):
    Ans = 0
    Ans = A + B
    return Ans
    
def main():
   if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()
        
   Ret = Addition(int(argv[1]), int(argv[2]))
        
   print("Addition is :",Ret)
        
if __name__ == "__main__":
    main()
    
    
    
    #           python AdditionCommand.py  10 20
    #     Output:   Addition is : 30