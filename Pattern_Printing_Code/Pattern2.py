*
*  *
*  *  *
*  *  *  *



def Display_Pattern():
    
    for i in range(1,5):
        for j in range(1,5):
            if(i >= j):
                print("*\t", end="")

        print()

def main(): 

    Display_Pattern()

if __name__ == "__main__":
    main()
