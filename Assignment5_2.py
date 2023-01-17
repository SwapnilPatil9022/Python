"""
 2. Write a program which contaice one class named as Circle.
	Circle class contains three instance variable as Radius, Area, Circumference.
	That class contains one class variable as PI which is initialise to 3.14.
	Inside init method initialise all instance variable as 0.0.
	There are three instance methods inside class as Accept(), CalculateArea(),
	 CalculateCircumference() , Display().
	- Accept() method will Accept value of Radius from user.
	- CalculateArea() method will Calculate area of Circle and store it into instance variable Area.
	- CalculateCircumference() method will Calculate circumference of circle and store it into 
		instance variable Circumference.
	- And Display() method will display value of all the instance variable as Radius, Area, Circumference.
	After designing the above class call all instance method by creating multiple objects. 
"""

class Circle:

	PI = 3.14

	def __init__(self):
		self.Radius = 0.0
		self.Area = 0.0
		self.Circumference = 0.0

	def Accept(self):
		print("Enter Radius of Circle is : ")
		self.Radius = float(input())
		return self.Radius

	def CalculateArea(self):
		self.Area = Circle.PI * self.Radius * self.Radius
		return self.Area
		
	def CalculateCircumference(self):
		self.Circumference = 2 * Circle.PI * self.Radius
		return self.Circumference

	def Display(self):
		print("Radius value of Circle is => ",self.Radius)
		print("CalculateArea of Circle is => ",self.Area)
		print("Circumference of Circle is => ",self.Circumference)


def main():
	Obj = Circle()

	Obj.Accept()
	Obj.CalculateArea()
	Obj.CalculateCircumference()
	Obj.Display()

if __name__ == "__main__":
	main()