"""
  1. Write a program which accepts file name from user and check whether that file exists in 
  	 current directory or not.

  	 Input : Demo.txt
  	 Check whether Demo.txt exists or not.
"""

import os

def Search_File(File_Name):
	print("Inside Search_File method")

	if(os.path.exists(File_Name)):
		print("File is already exists : "+File_Name)
	else:
		print("File in Not exists")

def main():
	print("Inside Main Method")

	Find_File = input("Enter the file that you want to store.\n")
	Search_File(Find_File)

if __name__ == "__main__":
	main()
