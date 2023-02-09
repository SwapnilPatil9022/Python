# Instance variable : Name, Amount, Address, AccountNo
# Instance method : CreateAccount(), DisplayAccountInfo()
# Class variable : Bank_Name ,ROI_On_FD

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
   
def main():

    print("Name of bank : ",Bank_Account.Bank_Name)
    print("Rate of Intrest on Fixed deposit : ",Bank_Account.ROI_On_FD)
    
    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Createing the first account")
    User1.CreateAccount()

    print("Createing the second account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()


if __name__ == "__main__":
    main()