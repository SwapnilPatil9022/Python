        # Backtraking
def Display(No):
    if(No > 0):
        No = No - 1
        Display(No)     # Recusive call     #Head recursion (Not the end line)
        print(No)
    
Display(4)
