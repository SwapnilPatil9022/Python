"""
# 4. Write a program which contaice filter(), map() and reduce() in it. Python application which
	containce one list of Numbers. List containce the number are accepted from user. Filter
	should filter should filter out such numbers which are even. Map function will calculate its square,
    Reduce will retrun addition of all that numbers.

	Input = [5,2,3,4,3,4,1,2,8,10]
	List after filter = [2,4,4,2,8,10]
	List after map = [4,16,16,4,64,100]
	Output of reduce = 204
"""

def CheckEven(No):
    return (No % 2 == 0)

def MultX(No):
    return No*No

def SumX(A,B):
	return A+B

def filterX(Helper_Function, Data):
    Result = []
    for No in Data:
        if(Helper_Function(No) == True):
            Result.append(No)
    return Result
    
def mapX(Helper_Function, Data):
    Result = []
    for No in Data:
        Value = Helper_Function(No)
        Result.append(Value)
    
    return Result

def reduceX(Helper_Function, Data):
    Ans = 0
    for no in Data:
        Ans = Helper_Function(Ans,no)
        
    return Ans 

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
    
    Data_Map = mapX(MultX, Data_Filter)
    print("Data after map is :",Data_Map)

    Output = reduceX(SumX, Data_Map)
    print("Data after reduce is :",Output)
    
if __name__ == "__main__":
    main()