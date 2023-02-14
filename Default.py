
def Area(Radius, PI = 3.14):
    Result = PI * Radius * Radius
    return Result

def main():
    RValue = 10.5
    PIValue = 3.14
    
    # Positional arguments
    Ans = Area(RValue,PIValue)      # Ans = Area(10.5, 3.14)
    print("Area of circle is :",Ans)
    
    # Keyword arguments
    Ans = Area(PI = PIValue, Radius = RValue)     
    print("Area of circle is :",Ans)
    
    # Positional agrument and Secound is Default
    Ans = Area(10.5)      # Ans = Area(10.5)
    print("Area of circle is :",Ans)
    
    # Keyword agrument and Secound is Default
    Ans = Area(Radius = 10.5)      # Ans = Area(10.5)
    print("Area of circle is :",Ans)
    
    # Keyword arguments
    Ans = Area(PI = 7.10, Radius = 10.5)      # Ans = Area(7.1, 10.5)
    print("Area of circle is :",Ans)
    
if __name__ == "__main__":
    main()
    
# 346.185