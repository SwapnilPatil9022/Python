def Add(A,B):
    return A+B
    
def Sub(A,B):
    return A-B

def main():
    print("Enter first number :")
    No1 = int(input())
    
    print("Enter Secound number :")
    No2 = int(input())
    
    Ans = Add(No1,No2)
    print("Additon is :",Ans)
    
    Ans = Sub(No1,No2)
    print("Substraction is :",Ans)
   
if __name__ == "__main__":
    main()