import schedule
import time
import datetime

def Task_Minutes():
	print("Task based on minutes scheduled on : ",datetime.datetime.now())

def Task_Hour():
	print("Task based on the hour's scheduled on : ",datetime.datetime.now())

def Task_Day():
	print("Task based on the day scheduled on : ",datetime.datetime.now())

def main():
	print("Inside task scheduler : ")
	print("Current time is : ",datetime.datetime.now())

	schedule.every(1).minutes.do(Task_Minutes)
	schedule.every(1).hour.do(Task_Hour)
	schedule.every(1).monday.at("18:56").do(Task_Day)

	while(True):
		schedule.run_pending()
		time.sleep(1)

if __name__ == "__main__":
	main()