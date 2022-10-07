print("Application to demonstrate Industrial programming")

def Addition(Value1, Value2):   #Bezness logic 
     Ans = Value1 + Value2
     return Ans

def main():
    print("Enter First number : ")
    no1 = int(input())
    print("Enter secound number : ")
    no2 = int(input())

    Sum = Addition(no1,no2)
    
    print("Addition is : ",Sum)
    
if__name__ == "__main__":
    main()