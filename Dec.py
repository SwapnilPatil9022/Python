# Swapping of two numbwes program  using Decorator Logic

from Dec2 import*
    

def main():                                     # 100
    Value1 = int(input("Enter first number : "))        # 8 cmd input
    Value2 = int(input("Enter secound number : "))      # 12 cmd input
     
    New_Function = Decorated_Function(Substraction) # Decorated_Function(200)
    
    Ret = New_Function(Value1,Value2) # Ret(300(8,12))
    print("Substraction is : ",Ret)
if __name__ == "__main__":
    main()                                     # call 100()
        