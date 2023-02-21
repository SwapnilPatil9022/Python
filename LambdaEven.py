def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False
        
def CheckEvenX(No):
    return (No % 2 == 0)
    
Ret = CheckEven(12)

if(Ret == True):
    print("Its even")
else:
    print("Its odd")