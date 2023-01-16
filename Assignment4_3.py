 """
# 3. Write a program which contaice filter(), map() and reduce() in it. Python application which
	containce one list of Numbers. List containce the number are accepted from user. Filter
	should filter out all such numbers which greter than or equal to 70 and less than or equal to
	90. Map function will increase each number by 10. Reduce will return product of all that numbers.

	Input = [4,34,36,76,68,34,89,23,86,90,45,70]
	List after filter = [76,89,86,90,90]
	List after map = [86,99,96,100,80]
	Output of reduce = 6538752000
"""

def CheckNum(No):
    return (No >= 70 and No <= 90)

def AddX(No):
    return No+10

def Mult(A,B):
	return A*B

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
    Ans = 1	
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
    
    Data_Filter = filterX(CheckNum, Data_Input)
    print("Data after filter is :",Data_Filter)
    
    Data_Map = mapX(AddX, Data_Filter)
    print("Data after map is :",Data_Map)

    Output = reduceX(Mult, Data_Map)
    print("Data after reduce is :",Output)
    
if __name__ == "__main__":
    main()