"""
1. Write a recursive program which Accept number from user and return summation of it's digits.
	Input :		879
	Output : 	24
"""
Add = 0
Dig = 0

def Summation(No):
	global Add
	global Dig
	if(No != 0):
		Dig = No % 10
		Add = Add + Dig
		No = No // 10
		Summation(No)
		return Add

def main():
	Value = 879

	Ret = Summation(Value)
	print("Summaion is : ",Ret)	

if __name__ == "__main__":
	main()
