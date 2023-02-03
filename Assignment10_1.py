"""
 1.	Design automation script with accept directory name and file extension from user. Display all 
 	files with that extension.

 	Usage : DirectoryFilSreach.py  Demo  ".txt"

 	Demo is name of directory and .txt is the extension that we want to search.
"""
import os
from sys import*

def Directory_Extention(path, extension):
	flag = os.path.isabs(path)
	if flag == False:
		path = os.path.abspath(path)

	exists = os.path.isdir(path)

	if exists:
		for foldername,subfolder,filename in os.walk(path):
			for filen in filename:
				if filen.lower().endswith(extension):
					print(filen)

	else:
		print("Invalid Path.")

def main():
	print("-----Directory traversal and find the file------")

	print("Applicatom name is : "+argv[0])

	if(len(argv) != 3):
		print("Invalid input")
		exit()

	if(argv[1] == "-h") or (argv[1] == "-H"):
		print("Help : This programs is find the .txt extension files")
		exit()

	if(argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage : Application_Name Directory_Name .extension")
		exit()

	Directory_Extention(argv[1],argv[2])

if __name__ == "__main__":
	main()