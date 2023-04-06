
def Display(No):
    Cnt = 0
    
    if(Cnt < No):
        print("Hello")
        Cnt = Cnt + 1
        Display(No)                         #Recursion statment

Display(4)