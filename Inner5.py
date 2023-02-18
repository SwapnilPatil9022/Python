# Swapping of two numbwes program  using Decorator Logic
def Substraction(No1,No2):   # 200                   # Abstract decorator
    Ans = No1 - No2
    return Ans
    
def Decorated_Function(Function_Name):  # Function_Name(200)
    def Inner(A,B):     # 300
        if(A < B):
            A,B = B,A               # swapping logic
            Output = Function_Name(A,B)     # 200(12,8)
        return Output
    return Inner        # return 300
    
def main():                                     # 100
    Value1 = int(input("Enter first number : "))        # 8 cmd input
    Value2 = int(input("Enter secound number : "))      # 12 cmd input
     
    New_Function = Decorated_Function(Substraction) # Decorated_Function(200)
    
    Ret = New_Function(Value1,Value2) # Ret(300(8,12))
    print("Substraction is : ",Ret)
if __name__ == "__main__":
    main()                                     # call 100()
       