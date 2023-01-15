# 2. Write a program which accept one number and Display below pattern
"""
    Input : 5
    
    Output : *  *   *   *   *
             *  *   *   *   *
             *  *   *   *   *
             *  *   *   *   *
             *  *   *   *   *
"""
def Display(No):
   
        for i in range(0,No):
            for j in range(0,No):
                print("*\t", end = " ")
            print()
    
def main():
    print("Please Enter the number :")
    Value = int(input())
    
    Ret = Display(Value)
    
if __name__ == "__main__":
    main()
