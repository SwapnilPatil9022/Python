"""
 3.	Design automation script which accept two directory names and copy all files from first directory
 	into secound directory. secound directory should be created at run time.

 	Usage : DirectoryFilSreach.py  "Demo"  "Temp" 

 	"Demo" is name of directory which is existing and contains file in it.
 	 We have to create new Directory as "Temp" and copy all files from Demo to Temp.
"""
import os
from sys import*
import shutil

def Directory_Copy(path):
	if(os.path.exists(path)):
		fd = open(path,"r")
		Data = fd.read()
		print("Data from the file is \n")
		print(Data)
		print("\n")

		fd.close()

	else:
		print("File is not existing")
		return

	NewFile = input("Please enter the new file name is \n")
	NF = open(NewFile,"a")

	shutil.copyfile(path,NewFile)
	
def main():
	print("-----Directory traversal and find the file------")

	print("Applicatom name is : "+argv[0])

	if(len(argv) != 2):
		print("Invalid input")
		exit()

	if(argv[1] == "-h") or (argv[1] == "-H"):
		print("Help : This programs is find the .txt extension files")
		exit()

	if(argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage : Application_Name Directory_Name .extension")
		exit()

	Directory_Copy(argv[1])

if __name__ == "__main__":
	main()
