"""
def main():
	Arr = list()

	print("Hown many element tyat you want to store list.")
	size = int(input())

	print("Please enter the element.")

	for i in range(0,size):
		no = int(input())
		Arr.append(no)

	print(Arr)


if __name__ == "__main__":
	main()

	"""

 class Value:

    def __init__(self,Data):
        self.No = Data

    def SumFactors(self):
        Sum = 0

        for i in range(1,self.No):
            if(self.No % i == 0):
                Sum = Sum + i
        
        return Sum

    def CheckPerfect(self):
        Ans = self.SumFactors()

        if(self.No == Ans):
            return True
        else:
            return False

def main():
    print("Please enter number")
    A = int(input())

    obj = Value(A)

    Ret = obj.CheckPerfect()
    if(Ret == True):
        print("{} is a perfect number".format(A))
    else:
        print("{} is not a perfect number".format(A))


if __name__ == "__main__":
    main()
