"""
 3. Write a program which contains one class named as Arithmetic.
	Arithematic class contains two instance variable as Value1, Value2.
	Inside init method initialise variable to 0.
	There are three instance method inside class as Accept(), Addition(), Substraction(),
	Multiplication(), Division().
	- Accept() method will accept value of Value1, Value2 from user.
	- Addition() method will perform addition of Value1, Value2 and return result.
	- Substraction() method will perform Substraction of Value1, Value2 and return result.
	- Multiplication() method will perform Multiplication of Value1, Value2 and return result.
	- Division() method will perform Division of Value1, Value2 and return result.
	- After designing the above class call all instance method by creating multiple objects.
 """

class Arithmetic:

	def __init__(self):
		Value1 = 0
		Value2 = 0
	      
	def Accept(self):
		self.Value1 = int(input("Enter the First number : "))
		self.Value2 = int(input("Enter the Secound number : "))

	def Addition(self):
		Add = self.Value1 + self.Value2
		print("Addition of two number is : ",Add)

	def Substraction(self):
		Sub = self.Value1 - self.Value2
		print("Substraction of two number is : ",Sub)

	def Multiplication(self):
		Mult = self.Value1 * self.Value2
		print("Multiplication of two number is : ",Mult)

	def Division(self):
		Div = self.Value1 / self.Value2
		print("Division of two number is : ",Div)

def main():
	obj = Arithmetic()

	obj.Accept()
	obj.Addition()
	obj.Substraction()
	obj.Multiplication()
	obj.Division()

if __name__ == "__main__":
	main()