def DisplayF(no):
	i = 1
	print("Factors are :")

	while(i <= int(no/2)+1):
		if no % i == 0:
			print(i)
		i = i + 1


		"'"
		
def CheckEven(No):
	return No % 2 == 0

def Increment(No):
	return No+2

def filterX(Arr,Function_Name):
	Result = []
	for no in Arr:
		if(Function_Name(no)):
			Result.append(no)
	return Result

def main():
	Data = list()

	print("Enter how many element you want to store in list :")
	size = int(input())

	print("please enter the values")

	for i in range(0,size):
		no = int(input())
		Data.append(no)
	print(Data)

	Data_Filter = list(filterX(Data,CheckEven))

	print("Data after filter :",Data_Filter)

if __name__ == "__main__":
	main()
