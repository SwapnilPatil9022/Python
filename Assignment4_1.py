# 1.Write a program which contains one lambda function which accepts one parameter and return power of two.

def main():

	Power = lambda No : 2**No

	print("Please Enter the number :")
	Value = int(input())

	Ans = Power(Value)

	print("Power using lambda function : ",Ans)

if __name__ == "__main__":
	main()