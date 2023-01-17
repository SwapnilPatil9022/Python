"""
 1.	Write a program which contains one class as BookStore.
 	BookStore class contains two instance variables as Name, Author.
 	That class contains one class variable as NoOfBooks which display name, Author and numebr of books.
 	Initialise instans variable in init method by accepting the values from user as name and author.
 	inside init method increment value of NoOfBooks by one.

 	After creating the class create the two objects of BookStore class as
 	Obj1 = BookStore("Linux System programming","Robert Love")
 	Obj1.Display()		# Linux System programming by Robert Love. No of Books : 1

 	Obj2 = BookStore("C programming","Dennis Ritchie")
 	Obj2.Display()		# C programming by Dennis Ritchie. No of books : 2
"""

class BookStore:

	NoOfBooks = 0

	def __init__(self):
		self.Name = input("\n Enter Book Name : ")
		self.Author = input("\n Enter Author Name : ")
		BookStore.NoOfBooks = BookStore.NoOfBooks + 1

	def Display(self):
		print("\n",self.Name,"by",self.Author,"No of Books : ",BookStore.NoOfBooks)

def main():
	Obj1 = BookStore()
	Obj1.Display()
	Obj2 = BookStore()
	Obj2.Display()

if __name__ == "__main__":
	main()