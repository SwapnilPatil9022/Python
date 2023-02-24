
class Numbers:
    def __init__(self):
        self.Size = 0
        self.Arr = list()
        self.Accept()
       
    def Accept(self):
        print("Enter how many elements you want : ")
        self.Size = int(input())
        
        print("Please enter the elements")
        Value = 0
        for i in range(0,self.Size):
            Value = int(input())
            self.Arr.append(Value)
            
    def Display(self):
        print("Elements from list are : ")
        for i in range(0,self.Size):
            print(self.Arr[i])

    def Summation(self):
        Sum = 0
        for i in range(0,self.Size):
            Sum = Sum + self.Arr[i]
            
        return Sum
        
    def Average(self):
        Sum = 0
        for i in range(0,self.Size):
            Sum = Sum + self.Arr[i]
            
        return (Sum/self.Size)
        
    def Maximun(self):
        Max = 0
        Max = self.Arr[0]
        for i in range(0,self.Size):
            if(self.Arr[i] > Max):
                Max = self.Arr[i]
            
        return Max
        
    def Minimum(self):
        Max = 0
        Max = self.Arr[0]
        for i in range(0,self.Size):
            if(self.Arr[i] < Max):
                Max = self.Arr[i]
            
        return Max

def main():
    obj = Numbers()
    obj.Display()
    
    Output = obj.Summation()
    print("summation of all elements is : ",Output)
	
    Output = obj.Average()
    print("Average of all elements is : ",Output)
	
    Output = obj.Maximun()
    print("Largest elements is : ",Output)
	
    Output = obj.Minimum()
    print("Smallest elements is : ",Output)
	
    
if __name__ == "__main__":
    main()