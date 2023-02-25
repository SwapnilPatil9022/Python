# Accept 2 numbers and perform addition and substraction of it

# Kay karayecha ahe?        -> Behaviours (Functions)
#   Addition ani Substraction

# Te karayeala kay laganar ahe?     -> Characteristics (Data)
#   2 numbers

# Class = Characteristics + Behaviours
# Class = Data + Functions


class Arithematic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Add(self):
        return self.No1+self.No2

    def Sub(self):
        return self.No1-self.No2

def main():
    print("Enter first number")
    Value1 = int(input())

    print("Enter second number")
    Value2 = int(input())

    obj = Arithematic(Value1,Value2)

    Ans = obj.Add()
    print("Addition is : ",Ans)

    Ans = obj.Sub()
    print("Substraction is : ",Ans)
    
if __name__ == "__main__":
    main()