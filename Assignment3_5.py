# 4. Write a program which accept N number from user and store it into List. Accept one another number from user and return additom of all prime number from list.
#	input :	 	Number of Elements : 11
#	Input elements : 13   5	  45   7   4   56   10	 34   2	  5   8
#	Output : 	54(13+5+7+2+5)

import MarvellousNum as M

def ListPrime(List):
	Prime_Lst = []
	Num = 0
	Ret = 0

	for i in List:
		Num = M.ChkPrime(i)
		if (Num == "Number is prime"):
			Prime_Lst.append(i)

	return Prime_Lst

def Add_Prime_Lst(List):
	Add = 0
	for i in range(len(List)):
		Add = Add + List[i]

	return Add

def main():
	List = []
	Ele = 0

	print("\nEnter Number of Elements =>")
	No = int(input())

	for i in range(0,No):
		Ele = int(input("\nEnter Elements =>"))
		List.append(Ele)

		print("\nGiven List is :",List)

		Ret = ListPrime(List)
		print("\nPrime List is :",Ret)

		Addition = Add_prime_List(ret)
		print("\nAddition of prime list is =>",Addition)

if __name__ == "__main__":
	main()
