

import pickle
f = open("C://python/pick.txt","rb")
d = pickle.load(f)
print(d)
f.close()





import pickle
f = open("C://python/pick.txt","wb")
dct = {"name" : "Swapnil", "age" : 23, "Gender" : "M", "marks" : 75}
pickle.dump(dct,f)
f.close()












"""
def Display(iNo):

	for i in range(1,iNo+1,):
		print("*",end = " ")

def main():
	Value = int(input("enter the number : "))

	Display(Value)

if __name__ == "__main__":
	main()
"""	















"""
def ChkEven(ino):

	if((ino % 5) == 0):
		print("Divisible ...")
	else:
		print("Not divisible ")

def main():
	iValue = int(input("enter the value...: "))

	iRet = ChkEven(iValue)

if __name__ == "__main__":
	main()
"""









"""
def Marvel():
	i = 5

	while(i >= 1):
		print(i,end = ' ')
		i = i - 1

def main():

	Marvel()

if __name__ == "__main__":
	main()
"""