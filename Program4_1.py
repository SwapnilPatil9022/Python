"""
 4.1 Writer a program which accept number from user and display its multiplication of factors.

 	Input : 12
 	Output : 144	(1*2*3*4*6)

	Input  : 13
	Output : 1		(1)
"""
def DisplayFact(No):
	
	cnt = 0
	Mult = 1

	for i in range(1,No):
		if No % i == 0:
			print(i)
			cnt = cnt + i
			Mult = i * Mult

	print("multiplication of factors :",Mult)

def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayFact(Value)

if __name__ == "__main__":
	main()
