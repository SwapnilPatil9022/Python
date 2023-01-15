from sys import *

def Addition(A,B):
    Ans = 0
    Ans = A + B
    return Ans

def main():
    print("Welcome to : ", argv[0])

    if(len(argv) == 2):
        if(argv[1] == "--U"):
            print("Use the application as : ")
            print("python Name_Of_Application First_number Second_number")
            exit()

        if(argv[1] == "--H"):
            print("Help : This application is used to perform addition of 2 numbers")
            exit()

    if(len(argv) != 3):
        print("Invalid number of arguments")
        print("Please use --U flag to get the usage")
        exit()
    
    Ret = Addition(int(argv[1]), int(argv[2]))

    print("Addition is : ",Ret)
    
    print("Thank you for using the application")
    print("Marvellous Infosystems by Piyush Manohar Khairnar")

if __name__ == "__main__":
    main()