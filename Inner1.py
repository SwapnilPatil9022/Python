def Hello():                                        # Outer function
    print("Inside Hello")
    
    def Demo():                                     # Inner function
        print("Inside Demo")
    
    Demo()
    
Hello()