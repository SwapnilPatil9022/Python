"""
# 4. Write a program which contaice filter(), map() and reduce() in it. Python application which
	containce one list of Numbers. List containce the number are accepted from user. Filter
	should filter should filter out all prime numbers. Map function will multiplay each number by 2,
    Reduce will retrun Maximum number  of all that numbers.

	Input = [2,70,11,10,17,23,31,77]
	List after filter = [2,11,17,23,31]
	List after map = [4,22,34,46,62]
	Output of reduce = 62
"""

def ChkPrime(Arr):
    Cnt = 0
    for i in range(2,Arr):
        if(Arr % i == 0):
            Cnt = Cnt + 1
            break
    
    if(Cnt != 0):
        return False
    else:
        return True

Increment = lambda No: No*2

def filterX(Arr,Function_Name):
    Result = []
    for no in Arr:
        if(Function_Name(no)):
            Result.append(no)
    return Result

def mapX(Arr,Function_Name):
    Result = []
    for no in Arr:
        value = Function_Name(no)
        Result.append(value)
    return Result

def reduceX(Arr):
    Max = 0
    Max = Arr[0]
    for i in range(0,len(Arr)):
        if(Arr[i] > Max):
            Max = Arr[i]
    return Max

def main():
    print("Enter number of elements you want to enter :")
    iSize = int(input())
   
    Data = []
    print("Please enter the data :")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data.append(Value)
        
    print("Data is :",Data)

    Data_FilterX = list(filterX(Data,ChkPrime))
    print("Data after filter :",Data_FilterX)

    Data_map = mapX(Data_FilterX,Increment)
    print("Data after map :",Data_map)

    Ret = reduceX(Data_map)
    print("Data after reduce :",Ret)

if __name__ == "__main__":
    main()


















