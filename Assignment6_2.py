"""
 2.	Write a program which contains one class as BankAccount.
 	BankAccount class contains two instance variables as Name & Amount.
 	That class contains one class variable as ROI which is initialise to 10.5.
 	inside init method initalise all name and amount variables by accepting the values from user.
 	There are Four instance methods inside class as Display(), Deposite(), Withdraw(), CalculateIntrest().
 	
 	- Deposite() method will accept amount from user and add that value in class instance variable Amount.
 	- Withdraw() method will accept the amount to be withdraw from user and subtrac that amount from 
 		class instance variable Amount.
 	- CalculateIntrest() method calculate the intrest based on Amount by considering rate of Intrest
 		which is Class variable as ROI.
	- Display() method will display value of all the instance variables as Name and Amount.
		After designing the above class call all instance methods by creating multiple Objects.
"""

class BankAccount:

	ROI = 10.5

	def __init__(self):
		self.Name = input("\n Enter the Name : ")
		self.Amount = float(input("\n Enter the Amount : "))

	def Deposite(self):
		self.Deposite_Amount = float(input("\n Enter your Deposite Amount : "))
		self.Amount = self.Deposite_Amount + self.Amount

	def Withdraw(self):
		self.Withdraw_Amount = float(input("\n Enter your Withdraw Amount : "))
		self.TotalAmount = self.Amount - self.Withdraw_Amount

	def CalculateIntrest(self):
		self.Rate_Of_Interest = self.TotalAmount * BankAccount.ROI

	def Display(self):
		print("------------Your Details-------------")
		print("\n Name : ",self.Name)
		print("\n Your Deposite Amount is : ",self.Amount)
		print("\n Your Withdraw Amount is : ",self.Withdraw_Amount)
		print("\n Your TotalAmount is : ",self.TotalAmount)
		print("\n ROI of Your Amount is : ",self.Rate_Of_Interest)
		print("------------Thank You----------------")

def main():
	Obj = BankAccount()

	Obj.Deposite()
	Obj.Withdraw()
	Obj.CalculateIntrest()
	Obj.Display()

if __name__ == "__main__":
	main()



