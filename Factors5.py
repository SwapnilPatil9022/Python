# import Numbers                             # OR
# from Numbers import DisplayFactors         # OR
# from Numbers import *                      # OR
import Numbers as NUM 

def main():
    print("Enter number :")
    No = int(input())
    
    NUM.DisplayFactors(No)

if __name__ == "__main__":
    main()