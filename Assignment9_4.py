"""
  4 . Write a program which accept two file name from user and campare contents of both the 
  	  files. if both the files contains same contents then display success otherwise display failure.
  	   Accept file name through command line argument.

  	Input : Demo.txt	Hello.txt	
  	compair contents of Demo.txt in Hello.txt
"""
from sys import*
import filecmp

def Create_New(First_File, Secound_File):
	print("First file name is ",First_File)
	print("------------------------------")	
	fd1 = open(First_File,"r")
	Data1 = fd1.read()
	print("Data is :\n",Data1)
	print("------------------------------")

	print("Secound file name is ",Secound_File)
	print("------------------------------")
	fd2 = open(Secound_File,"r")
	Data2 = fd2.read()
	print("Data is : \n",Data2)
	print("------------------------------")

	if (filecmp.cmp(First_File, Secound_File)):
		print("Result of compairing is : Success")
	else:
		print("Result of compairing is : failure")

def main():
	print("-----Inside Main method-----")
	print("----------------------------")

	print("Application Name is :"+argv[0])
	
	if(len(argv) != 3):
		print("Invalid argument")
		exit()

	Create_New(argv[1],argv[2])

if __name__ == "__main__":
	main()

