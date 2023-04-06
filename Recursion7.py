#4
# 4 + 3 + 2 + 1 =>  10

def Add(No):
    Ans = 0
    while(No >= 0):
        Ans = Ans + No
        No = No - 1
    return Ans
    
Ret = Add(4)

print("Result is : ",Ret)