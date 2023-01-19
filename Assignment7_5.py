"""
 3. Design python appliction which creates three threads as thread1 and thread2. Thread1 display 1 to 50
 	on scrren and thread2 display 50 to 1 in reverse order on screen. After execution of thread1 gets 
 	complited then schedule thread2.
"""
import threading
import time
	
def Thread1():
	No = 50
	for i in range(1,int(No)+1):
		print(i, end = " ")
	print("------------------")

def Thread2():
	i = 50
	while(i >= 1):
		print(i, end = " ")
		i = i - 1
	print("------------------")

def main():

	FirstThread = threading.Thread(target = Thread1)
	SecoundThread = threading.Thread(target = Thread2)

	FirstThread.start()
	time.sleep(5)
	FirstThread.join()

	SecoundThread.start()
	time.sleep(1)
	SecoundThread.join()

if __name__ == "__main__":
	main()

