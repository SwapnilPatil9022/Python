"""
 1. Design python application which creates two thread named as even and odd. Even thread will display 
 	first 10 even numbers and odd thread will display first 10 odd numbers.
"""

import os
import threading

def DisplayEven(No):
	print("PID of Even : ",os.getpid())
	for i in range(1,No+1):
		if (i % 2 == 0):
			print("Even Number is : ",i)

def DisplayOdd(No):
	print("PID of Odd : ",os.getpid())
	for i in range(1,No+1):
		if(i % 2 != 0):
			print("Odd Number is : ",i)

def main():
	print("PID of Main : ",os.getpid())
	Value = 20

	p1 = threading.Thread(target = DisplayEven, args = (Value,))
	p2 = threading.Thread(target = DisplayOdd, args = (Value,))

	p1.start()
	p1.join()

	p2.start()
	p2.join()

if __name__ == "__main__":
	main()
