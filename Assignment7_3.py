"""
 3. Design python appliction which creates two threads as evenlist and oddlist. Both the threads accept
 	list of integers as parameter. Evenlist thread add all even elements from input list and dipslay the 
 	addition. Oddlist thread add all odd elements from input list and display the addition.
"""

import threading 

def evenlist(Brr):
	Add = 0
	for i in range(len(Brr)):
		if(Brr[i] % 2 == 0):
			Add = Add + Brr[i]
	print("Addition of evenlist is : ",Add)

def oddlist(Brr):
	Add = 0
	for i in range(len(Brr)):
		if(Brr[i] % 2 != 0):
			Add = Add + Brr[i]
	print("Addition of oddlist is : ",Add)

def main():
	Arr = []
	Ele = 0

	No = int(input("Enter the number of elements : "))

	for i in range(No):
		Value = int(input("Enter the list parameter : "))
		Arr.append(Value)

	print("Parameter of given list are : ",Arr)

	Evenlist_Thread = threading.Thread(target = evenlist, args = (Arr,))
	Oddlist_Thread = threading.Thread(target = oddlist, args = (Arr,))

	Evenlist_Thread.start()
	Oddlist_Thread.start()

	Evenlist_Thread.join()
	Oddlist_Thread.join()

if __name__ == "__main__":
	main()

