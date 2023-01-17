"""
 1.	Write a program which contains one class named as Demo.
 	Demo class contains two instance variable as no1,no2.
 	That class contains one class variable as Value.
 	There are two instance methods of class as Fun and Gun which display values of instance variables.
 	Initialise instance variable in init method by accepting the values from user.
	
 	After creating the class create the two objects of Demo class as
 	Obj1 = Demo(11,21)
 	Obj2 = Demo(51,101)

 	Now call the instance method as
 	Obj1.Fun()
 	Obj2.Fun()
 	Obj1.Gun()
 	Obj2.Gun()
"""

class Demo:

	Value = 0

	def _init__(self,No1,No2):
		print("Inside init method :")
		self.No1 = 0
		self.No2 = 0

	def Fun(self):
		self.No1 = int(input("Enter the First number of Fun method : "))
		print(self.No1)

		self.No2 = int(input("Enter the Secound number of Fun method : "))
		print(self.No2)

	def Gun(self):
		self.No1 = int(input("Enter the First number of Gun method : "))
		print(self.No1)

		self.No2 = int(input("Enter the Secound number of Gun method : "))
		print(self.No2)
		
def main():

	Obj1 = Demo()
	Obj2 = Demo()

	print("Demonstration of Obj1")

	Obj1.Fun()
	Obj1.Gun()

	print("Demonstration of Obj2")

	Obj2.Fun()
	Obj2.Gun()

if __name__ == "__main__":
	main()