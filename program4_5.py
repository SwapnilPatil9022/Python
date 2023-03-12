

"""
 4.5 Writer a program which accept number from user and return display between summation of all factors and non factors.

 	Input : 12
 	Output : -34	(16 - 50)

	Input  : 10
	Output : -29	(8 - 37)
"""
def DisplayDiffSum(No):
	cnt = 0
	mult = 1

	for i in range(1,No+1):
		if (No % i) != 0:
			print(i)
			cnt = cnt + i
	print(cnt)
		
	print("\n--------------\n")

	cnt1 = 0
	for i in range(1,No):
		if No % i == 0:
			print(i)
			cnt1 = cnt1 + i
	print(cnt1)

	result = cnt1 - cnt
	print("Result is ",result)
	
def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayDiffSum(Value)

if __name__ == "__main__":
	main()


