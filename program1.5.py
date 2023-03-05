# 5. Write a program which display 10 to 1 on screen.
# Output : 10   9   8   7   6   5   4   3   2   1

def main():
    iNo = 10
    
    for i in range(0,10):       #using for loop.         
        print(iNo)
        iNo = iNo - 1

if __name__ == "__main__":
    main()

"""
def main():
    iNo = 10
    
    while iNo > 0:          # Using while loop
        print(iNo)
        iNo = iNo - 1
        
if __name__ == "__main__":
    main()
"""
   