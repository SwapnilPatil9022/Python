
def Display(No):
    if(No > 0):
        print(No)
        No = No - 1
        Display(No)     #Recursive call     #teal recursion (bexouse this is at end line)
    
Display(4)



"""
or

def Display(No):
    if(No > 0):
        print(No)
        Display(No - 1)     #Recursive call
    
Display(4)
