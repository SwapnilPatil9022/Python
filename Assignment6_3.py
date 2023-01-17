"""
 3.	Write a program which contains one class as Numbers.
 	Arithmetic class contains one instance variables as Value.
 	Inside init method initalise that instance variables to the value which is accepted from user.
 	There are Four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), Factors().

 	- ChkPrime() method will return true if number is prime otherwise return false.
 	- ChkPerfect() method will returns true if number is perfect otherwise return false.
	- Factors() method will display all factors of instance variable.
	- SumFactors() method will return addition of all factors. Use this method in any
		another method as a helper method if required.
	- After designing the above class call all instance methods by creating multiple objects. 
"""
class Numbers:
    
    def __init__(self):
        self.Value = int(input("Enter a Number =>"))
        
    def ChkPrime(self):
        Cnt = 0
        for i in range(2,self.Value):
            if(self.Value % i == 0):
                Cnt = Cnt + 1
                
        if(Cnt == 0):
            print("True")
            print("Its Prime number.")
        else:
            print("False")
            print("Not a Prime number.")
    
    def ChkPerfect(self): 
        No = 0
        
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                No = No + i
                
        if(No == self.Value):
            print("True")
            print("Its Perfect Number.")
        else:
            print("False")
            print("Not a perfect Number.")
    
    def Factors(self):        
        for i in range(2,self.Value):
            if(self.Value % i == 0):
                print(i)
    
    def SumFactors(self):        
        Num = 0
        
        for i in range(2,self.Value):
            if(self.Value % i == 0):
                Num = Num + i
            
        print(Num)
         
        
def main():
    obj = Numbers()    
    if(obj.Value == 1):
        print("Enter Valid Number")
    
    else:
        print("\n-----Check Given Number is Prime or Not-----")
        obj.ChkPrime()
        
    print("\n-----Check Given Number is Perfect or Not-----")            
    obj.ChkPerfect()
    
    print("\n-----Print Factors of Given Number-----")    
    obj.Factors()
    
    print("\n-----Sum of Factors of Given Number-----")    
    obj.SumFactors()
      
if __name__ == "__main__":
    main()

