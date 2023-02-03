"""
 2.	Design automation script with accept directory name and two file extension from user. From user 
 	rename all files with first file extension with the secound file extension.

 	Usage : DirectoryFilSreach.py  "Demo"  ".txt" 

 	Demo is name of directory and .txt is the extension that ew want to search and rename with .doc.
"""
import os
from sys import*

def Directory_Extention(path, extension, extension1):
	flag = os.path.isabs(path)
	if flag == False:
		path = os.path.abspath(path)

	exists = os.path.isdir(path)

	if exists:
		for foldername,subfolder,filename in os.walk(path):
			for filen in filename:
				if filen.lower().endswith(extension):
					pass

		for fn in os.listdir(path):
			infilename = os.path.join(path, fn)
			if not os.path.isfile(infilename): continue
			oldbase = os.path.splitext(fn)
			newname = infilename.replace(extension, extension1)
			output = os.rename(infilename, newname)

	else:
		print("Invalid Path.")

def main():
	print("-----Directory traversal and find the file------")

	print("Applicatom name is : "+argv[0])

	if(len(argv) != 4):
		print("Invalid input")
		exit()

	if(argv[1] == "-h") or (argv[1] == "-H"):
		print("Help : This programs is find the .txt extension files")
		exit()

	if(argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage : Application_Name Directory_Name .extension")
		exit()

	Directory_Extention(argv[1],argv[2],argv[3])

if __name__ == "__main__":
	main()


