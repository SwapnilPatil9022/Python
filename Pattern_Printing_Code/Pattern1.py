
Display Pattern : 
iRow = 5
iCol = 5

@  @  @  @
@  #  #  @
@  #  #  @
@  @  @  @


def Display(iRow, iCol):
    
    for i in range(1,iRow):
        for j in range(1,iCol):
            if i == 1 or j == 1 or j == 4 or i == 4:
                print("@", end="\t")
            else:
                print("*", end="\t")

        print()

def main():
    iRow = int(input("Enter iRow : "))
    iCol = int(input("Enter iCol : "))

    Display(iRow, iCol)

if __name__ == "__main__":
