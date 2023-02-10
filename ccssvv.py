import csv

def Create():
	with open('details.csv',"w")as obj:
		fobj = csv.writer(obj)
		fobj.writerow(["Roll","Name","Total"])
		while True:
			Roll = int(input("Enter Roll number : "))
			Name = input("Enter name : ")
			Total = int(input("Enter total mark : "))
			Record = ["Roll,Name,Total"]
			fobj.writerow(Record)

			ch = int(input("1->Enter More \n 2-> exit\n enetr your choice :"))

			if(ch == 2):
				break

def Search():
	with open('details.csv',"r")as obj:
		fobj = csv.reader(obj)
		next(fobj)

		for i in fobj:
			if((i[2]) >= 99):
				print(i)


def Display():
	with open("details.csv","r") as obj:
		fobj = csv.reader(obj)

		for i in fobj:
			print(i)

def main():


	Create()
	Display()
	Search()

if __name__ == "__main__":
	main()
