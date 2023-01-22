"""
  3 . Write a program which accept file name from user and create a new file named as Demo.txt and
  	  copy all contents from existing file into new file. Accept file name through command line argument.

  	Input : ABC.txt
  	Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt
"""
from sys import*

def Create_New(First_File):
	print("First file name is ",First_File)
	fd = open(First_File,"r")
	Data = fd.read()
	print(Data)

	name = input("Enter the new file name : \n")
	fd1 = open(name,"w")

	for Data in name:
		fd1.write(Data)

def main():
	print("-----Inside Main method-----")

	print("Application Name is :"+argv[0])
	
	if(len(argv) != 2):
		print("Invalid argument")
		exit()

	Create_New(argv[1])

if __name__ == "__main__":
	main()

