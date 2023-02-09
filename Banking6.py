# Instance variable : Name, Amount, Address, AccountNo
# Instance method : CreateAccount(), DisplayAccountInfo()
# Class variable : Bank_Name ,ROI_On_FD
# Class method : DisplayBankInformation
# Static method : DisplayKYCInfo

class Bank_Account:
    
    Bank_Name = "HDFC bank PVT LTD"
    ROI_On_FD = 6.7

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name : ")
        self.Name = input()

        print("Enter your intial amount : ")
        self.Amount = int(input())

        print("Enter your Address : ")
        self.Address = input()

        print("Enter your Account Number : ")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("-------- Your Account informartion is as below --------")
        print("Name of Account Holder : ",self.Name)
        print("Account Number : ",self.AccountNo)
        print("Address of Account Holder : ",self.Address)
        print("Current Amount in account : ",self.Amount)

    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to banking console")
        print("Name of our bank is : ",cls.Bank_Name)
        print("Rate of intrest we offer on fixed deposite is : ",cls.ROI_On_FD)
   
    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below KYC information")
        print("According to the rules of Goverment of India you have to submit below documnets")
        print("1 : Clear and recent passport size photo")
        print("2 : Photo of aadhar card")
        print("3 : Photo of PAN card")
       
    def Deposit(self,value):
        self.Amount = self.Amount + value

    def Withdraw(self,value):
        self.Amount = self.Amount - value

def main():
    print("----------------------------------------------------------------")
    print("---------- Banking Application ----------")
    print("----------------------------------------------------------------")
    print("---------- Calling Static method to display KYC info ---------- ")
    Bank_Account.DisplayKYCInfo()
    
    print("----------------------------------------------------------------")
    print("---------- Accessing the class variables from main ----------")
    print("----------------------------------------------------------------")
    print("Name of bank : ",Bank_Account.Bank_Name)
    print("Rate of Intrest on Fixed deposit : ",Bank_Account.ROI_On_FD)

    print("----------------------------------------------------------------")
    print("---------- Calling the class method to display Bank informatrion ----------")
    print("----------------------------------------------------------------")
    Bank_Account.DisplayBankInformation()

    print("----------------------------------------------------------------")
    print("---------- Creating the objects of class ----------")
    print("----------------------------------------------------------------")
    User1 = Bank_Account()
    User2 = Bank_Account()

    print("----------------------------------------------------------------")
    print("Createing the first account")
    print("----------------------------------------------------------------")

    print("----------------------------------------------------------------")
    print("---------- Enter details for first account holder ----------")
    print("----------------------------------------------------------------")
    User1.CreateAccount()

    print("----------------------------------------------------------------")
    print("Createing the second account")
    print("----------------------------------------------------------------")

    print("----------------------------------------------------------------")
    print("---------- Enter details for second account holder ----------")
    User2.CreateAccount()
    print("----------------------------------------------------------------")

    print("---------- Calling instance method to display information of first account ----------")
    User1.DisplayAccountInfo()

    print("---------- Calling instance method to display information of second account ----------")
    User2.DisplayAccountInfo()

    print("---------- Depositing 500 in User1 ----------")
    User1.Deposit(500)
    print("---------- Depositing 1200 in User2 ----------")
    User2.Deposit(1200)

    print("Amount of {} after deposit is {}: ".format(User1.Name,User1.Amount))
    print("Amount of {} after deposit is {}: ".format(User2.Name,User2.Amount))

    print("---------- Withdraw 200 in User1 ----------")
    User1.Withdraw(200)
    
    print("---------- Withdraw 3000 in User2 ----------")
    User2.Withdraw(3000)

    print("Amount of {} after withdraw is {}: ".format(User1.Name,User1.Amount))
    print("Amount of {} after withdraw is {}: ".format(User2.Name,User2.Amount))

    print("----------------------------------------------------------------")
    print("---------- End of banking appplication ----------")
    print("----------------------------------------------------------------")

if __name__ == "__main__":
    main()