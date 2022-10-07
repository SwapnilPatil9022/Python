print("Application to demonstrate Industrial programming")

import MarvellousModule

def main():
    print("Value of __name__ from main is : ",__name__)             # __main__          Special variable
    print("Enter First number : ")
    no1 = int(input())
    print("Enter secound number : ")
    no2 = int(input())

    Sum = MarvellousModule.Addition(no1,no2)
    
    print("Addition is : ",Sum)
    
if__name__ == "__main__":
    main()