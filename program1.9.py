# 9. Write a program which display first 10 even number on screen.
#   Output : 2  4   6   8   10  12  14  16  18  20

def main():
    iCnt = 2
    
    while iCnt <= 20:               # Using while loop
        print(iCnt)
        iCnt = iCnt + 2

if __name__ == "__main__":
    main()



"""
def main():
    iCnt = 2
    
    for i in range(0,20,2):         # Using  for loop
        print(iCnt)
        iCnt = iCnt + 2

if __name__ == "__main__":
    main()
"""