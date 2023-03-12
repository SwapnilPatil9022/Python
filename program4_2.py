"""
 4.2 Writer a program which accept number from user and display its factors in decressing order.

 	Input : 12
 	Output : 6 4 3 2 1 

	Input  : 10
	Output : 5 2 1
"""
def DisplayFactRev(No):
	
	cnt = 0

	for i in range(No-1,0,-1):
		if No % i == 0:
			print(i, end= " ")
			cnt = i - cnt

def main():
	print("Please enter the number :")
	Value = int(input())

	DisplayFactRev(Value)

if __name__ == "__main__":
	main()

