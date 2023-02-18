
def Outer():                    #100
    print("Inside Outer")
    
    def Inner():                #200
        print("Inside Inner")
    
    print(id(Inner))
    return Inner                #return 200
        
ret = Outer()                   # ret = 100
print(type(ret))
print(id(ret))
ret()                           # 200()
