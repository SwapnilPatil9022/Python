# 7. Write a program which containce one function that accept one number from user and return true if number is divisible by 5 otherwise return false.
#   Input : 8       Output : False
#   Input : 25       Output : True

def Chk(iNo):
    if iNo % 5 == 0:
        print("True")
    else:
        print("False")
    
def main():
    print("Please Enter the number :")
    iValue = int(input())
    
    Chk(iValue)

if __name__ == "__main__":
    main()