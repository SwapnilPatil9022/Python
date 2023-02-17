# Function which accept nothing and return nothing
def Demo1():
    print("Inside Demo1")

# Function accept one parameter and return nothing
def Demo2(No):
    print("Inside Demo2 with argument : ",No)

# Function accept one parameter and  addition of return value
def Demo3(No):
    print("Inside Demo3 with agreument",No)
    return No+2
    
# Function accept two parameter and return one parameter.
def Demo4(No1,No2):
    print("Inside Demo4")
    Add = No1 + No2
    return Add
    
# Function accept two parameter and return two parameter.
def Demo5(No1,No2):
    print("Inside Demo5")
    Add = No1 + No2
    Sub = No1 - No2
    return Add,Sub
    
def main():
    Demo1()
    Demo2("Hello")
    Ans = Demo3(10)
    print("Return value of Demo3 is :",Ans)
    Ans = Demo4(10,11)
    print("Return Value is :",Ans)
    Ans1,Ans2 = Demo5(10,11)
    print("First return value :",Ans1)
    print("Secound return value :",Ans2)
        
if __name__ == "__main__":
    main()
    
