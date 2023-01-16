# 2.Write a program which contains one lambda function which accepts two parameter and return its Multiplication.

def main():

	Mult = lambda No1,No2 : No1 * No2

	print("Please Enter First number :")
	Value1 = int(input())

	print("Please Enter Secound number :")
	Value2 = int(input())

	Ans = Mult(Value1,Value2)

	print("Multiplication using lambda function : ",Ans)

if __name__ == "__main__":
	main()