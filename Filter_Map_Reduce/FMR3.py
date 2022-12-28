
def CheckEven(No):
    return (No % 2 == 0)
    
def filterX(Helper_Function, Data):
    Result = []
    for No in Data:
        if(Helper_Function(No) == True):
            Result.append(No)
    return Result
    
def main():
    print("Enter number of elements you want to enter :")
    iSize = int(input())
   
    Data_Input = []
    print("Please enter the data :")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
        
    print("Data is :",Data_Input)
    
    Data_Filter = filterX(CheckEven, Data_Input)
    
    print("Data after filter is :",Data_Filter)
    
if __name__ == "__main__":
    main()