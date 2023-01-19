"""
 3. Design python appliction which creates three threads as small, capital, digits. All the thread
 	accept string as parameter. Small thread display number of small characters, capital thread are 
 	display capital character and digits thread display number of digits.
 	 Display id and name of each thread.
"""

import os
import threading

def small(str):
	print("\nThread Name of small is : ",threading.current_thread().name)
	print("\nPID of small is :",os.getpid())
	Cnt = 0
	for i in range(len(str)):
		if(str[i] >= 'a' and str[i] <= 'z'):
			Cnt = Cnt + 1
	print("Small letters are : ",Cnt)

def capital(str):
	print("\nThread Name of capital is : ",threading.current_thread().name)
	print("\nPID of capital is :",os.getpid())
	Cnt = 0
	for i in range(len(str)):
		if(str[i] >= 'A' and str[i] <= 'Z'):
			Cnt = Cnt + 1
	print("capital letters are : ",Cnt)

def digits(str):
	print("\nThread Name of digits is : ",threading.current_thread().name)
	print("\nPID of digits is :",os.getpid())
	Cnt = 0
	for i in range(len(str)):
		if(str[i] >= '0' and str[i] <= '9'):
			Cnt = Cnt + 1
	print("Digits are : ",Cnt)

def main():
	Value = input("Enter the data : ")

	Small_thread = threading.Thread(target = small, args = (Value,))
	Capital_thread = threading.Thread(target = capital, args = (Value,))
	Digits_thread = threading.Thread(target = digits, args =(Value,))

	Small_thread.start()
	Small_thread.join()

	Capital_thread.start()
	Capital_thread.join()

	Digits_thread.start()
	Digits_thread.join()

if __name__ == "__main__":
	main()