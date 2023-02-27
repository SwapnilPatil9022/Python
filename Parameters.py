# Positional Arguments   /   Keyword Arguments
def Add(No1,No2):
    print("Value of No1 :",No1)
    print("Value of No2 :",No2)
    return No1 + No2

def Sub1(No1,No2):
    print("Value of No1 :",No1)
    print("Value of No2 :",No2)
    return No1 - No2

def main():
    Ans = Add(10,11)                # Positional Arguments
    print("Addition is :",Ans)
    
    Ans = Sub1(No2 = 10,No1 = 11)       # Keyword arguments
    print("Addition is :",Ans)
    
    Ans = Sub1(No1 = 10,No2 = 11)       # Keyword arguments
    print("Addition is :",Ans)

if __name__ == "__main__":
    main()