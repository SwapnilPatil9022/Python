	import os 
from sys import*

def Directory_Watcher(Dir_Name):
	print("Inside Directory Watcher method")
	print("Name of input directory : ",Dir_Name)

	for foldername, subfolder, filenames in os.walk(Dir_Name):
		print("Folder Name is : "+foldername)
		for subf in subfolder:
			print("SubFolder Name of "+foldername+" is "+subf)
		for fnames in filenames:
			print("File inside folder "+foldername+" is "+fnames)
		print(" ")

def main():
	print("Directory watcher application")

	if(len(argv) < 2):
		print("Insufficient argument")
		exit()

	if(argv[1] == "-h") or (argv[1] == "-H"):
		print("This script will travel the directory and display the names of all entries")
		exit()

	if(argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage : Application_Name Directory_Name")
		exit()

	Directory_Watcher(argv[1])

if __name__ == "__main__":
	main()