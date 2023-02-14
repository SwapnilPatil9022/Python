import os
import multiprocessing

def Square(No):
    print("PID of worker process is {} for the input {}".format(os.getpid(), No))
    return (No*No)

def main():
	print("Proces of ID of our appication is : ",os.getpid())

	Data = [1,2,3,4,5]
	Result = []
 
	pobj = multiprocessing.Pool()
	Result = pobj.map(Square,Data)

	print("REsult after squarr is : ",Result)

if __name__ == "__main__":
	main()



"""
def Square(No):
	return (No*No)

def main():
	Data = [1,2,3,4,5]
	Result = []

	for Value in Data:
		Result.append(Square(Value))

	print("REsult after squarr : ",Result)

if __name__ == "__main__":
	main()
"""

"""
import os

def main():
	print("PID of current process is : ",os.getpid())
	print("PID of parent process is : ",os.getppid())

if __name__ == "__main__":
	main()
"""

"""
import multiprocessing

def main():
	print("Number of cores are : ",multiprocessing.cpu_count())

if __name__ == "__main__":
	main()
"""




"""


class Bank_Account:
	Bank_Name = "HDFC bank PVT LTD"
	ROI_On_FD = 6.7

	def __init__(self):
		self.Name = ""
		self.Amount = 0
		self.Address = ""
		self.AccountNo = 0

	def CreateAccount(self):
		print("Enter Your Name : ")
		self.Name = input()

		print("Enter your initial amount : ")
		self.Amount = int(input())

		print("Enter your Address : ")
		self.Address = input()

		print("Enter your Account number : ")
		self.AccountNo = int(input())

	def DisplayInfo(self):
		print("--------------------------------------")
		print("Name of account holder : ", self.Name)
		print("--------------------------------------")
		print("Account number is : ", self.AccountNo)
		print("--------------------------------------")
		print("Address of Acount holder : ", self.Address)
		print("--------------------------------------")
		print("Currunt amount account holder : ", self.Amount)	
		print("--------------------------------------")	

	@classmethod
	def DisplayBankInfo(cls):
		print("Welcome to banking console : ")
		print("Name of Bank : ",cls.Bank_Name)
		print("Rate of intrest : ",cls.ROI_On_FD)

	@staticmethod
	def DisplayKYCInfo():
		print("Please consider below KYC information : ")
		print("Accouding to the rules of Goverment of india you hava to submit below document " )
		print("1 : clear and recent passport size photo.")
		print("2 : Photo of aadhar card,")
		print("3 : Photo of PAN card.")

	def Deposit(self,Value):
		self.Amount = self.Amount + Value

	def Withdraw(self,Value):
		self.Amount = self.Amount - Value

def main():
	Bank_Account.DisplayBankInfo()
	Bank_Account.DisplayKYCInfo()

	User1 = Bank_Account()
	User2 = Bank_Account()

	print("Creting the first account : ")
	User1.CreateAccount()
	print("Creting the secound account : ")
	User2.CreateAccount()

	User1.DisplayInfo()
	User2.DisplayInfo()

	User1.Deposit(2000)
	User2.Deposit(6000)

	print("Amount of {} after Deposit is {} : ".format(User1.Name,User1.Amount))
	print("Amount of {} after Deposit is {} : ".format(User2.Name,User2.Amount))

	User1.Withdraw(1000)
	User2.Withdraw(3000)

	print("Amount of {} after Withdrow is {} : ".format(User1.Name,User1.Amount))
	print("Amount of {} after Withdraw is {} : ".format(User2.Name,User2.Amount))


if __name__ == "__main__":
	main()


"""
















"""
class Bank_Account:

	def __init__(self):
		self.Name = ""
		self.Amount = 0
		self.Address = ""
		self.AccountNo = 0

	def CreateAccount(self):
		print("Enter Your Name : ")
		self.Name = input()

		print("Enter your initial amount : ")
		self.Amount = int(input())

		print("Enter your Address : ")
		self.Address = input()

		print("Enter your Account number : ")
		self.AccountNo = int(input())

	def DisplayInfo(self):
		print("--------------------------------------")
		print("Name of account holder : ", self.Name)
		print("--------------------------------------")
		print("Account number is : ", self.AccountNo)
		print("--------------------------------------")
		print("Address of Acount holder : ", self.Address)
		print("--------------------------------------")
		print("Currunt amount account holder : ", self.Amount)	
		print("--------------------------------------")	

def main():
	User1 = Bank_Account()
	User2 = Bank_Account()

	User1.CreateAccount()
	User2.CreateAccount()

	User1.DisplayInfo()
	User2.DisplayInfo()


if __name__ == "__main__":
	main()

"""