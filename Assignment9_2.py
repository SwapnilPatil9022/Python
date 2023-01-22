"""
  2 . Write a program which accept file name from user and open that file and display the contents of 
  		that file on screen.
  	Input : 	Demo.txt
  	Display contents of Demo.txt on console.
"""
import os

def Display_Contents(File_Name):

	if (os.path.exists(File_Name)):
		print("File Name is : "+File_Name)
		fd = open(File_Name,"r")
		Data = fd.read()
		print("contents of file is :\n"+Data)
	else:
		print("File is Not exists")

def main():
	print("Inside Main method")

	File = input("Enter the file name that you want to Read \n")

	Display_Contents(File)

if __name__ == "__main__":
	main()