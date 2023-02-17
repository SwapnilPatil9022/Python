# Accept number from user and find factores of that number

def  DisplayFactors(No):
    i = 1
    print("Factors are : ")
    while(i <= int(No/2)):                      # Using While loop
        if((No % i) == 0):
            print(i)
        i = i + 1
    
def main():
    print("Enter number :")
    No = int(input())
    
    DisplayFactors(No)

if __name__ == "__main__":
    main()