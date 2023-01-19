"""
 2. Design python application which creates two threads as evenfactor and oddfactor.
  Both the thread accept one parameter as integer. Evenfactor thread will display addition of 
  even factor of given number and oddfactor will display addition of odd factors of given numbers.
  After execution of both the thread gets completed main thread should be display message as
  "exit from main".
"""

import threading

def EvenFactor(No):
	Add = 0
	for i in range(1,int(No/2)+1):
		if(i % 2 == 0):
			Add = Add + i
			print("Even factors is :",i)
	print("----------------------------------")
	print("Addition of even factors is : ",Add)
	print("----------------------------------")
		
def OddFactor(No):
	Add = 0
	for i in range(1,int(No/2)+1):
		if(i % 2 != 0):
			Add = Add + i
			print("Odd factors is :",i)
	print("----------------------------------")
	print("Addition of odd factors is : ",Add)
	print("----------------------------------")	

def main():
	print("Enter the number : ")
	Value = int(input())

	p1 = threading.Thread(target = EvenFactor, args = (Value,))
	p2 = threading.Thread(target = OddFactor, args = (Value,))

	p1.start()
	p1.join()

	p2.start()
	p2.join()

if __name__ == "__main__":
	main()
	print("exit from main")