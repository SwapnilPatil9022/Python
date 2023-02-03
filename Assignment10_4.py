"""
  4.Design automation script which accept two directory names and one file extension. copy all files
  	with the specified extension from first directory into secound directory. Secound dirctory shuld 
  	be create at the run time.

  	Usage : DirectoryCopyExt.py	"Demo" 	"Temp"	".exe"

  	Demo is name of directory which is existing and containcs file in it. We have to create new directory
  	as Temp and copy all files whith extension .exe from Demo to Temp.
"""
from sys import*
import os
import shutil
import glob

def DirectoryCopyExt(Dir, extension1):
	if(os.path.exists(Dir)):
		print("Directory name is : ",Dir)

		print("-----------------------------------------------------------")
		print("Please enter the name of Dircetory that you want to create :")
		NewDir = input()
		os.mkdir(NewDir)
		if (os.path.exists(NewDir)):
			print("Directory succesfully created ")

		print("----------------------------------------------------------")
		for foldername,subfolder,filename in os.walk(Dir):
			for filen in filename:
				if filen.lower().endswith(extension1):
					print(filen)
					shutil.copy2(os.path.join(Dir,filen),NewDir)
		print("\nFile is succesfully copied into the Temp folder\n")
		print("-----------------------------------------------------------")
		
	else:
		print("File not found...")

def main():
	print("-------Automation script of directory copy extension with file--------")

	print("Application name is : "+argv[0])

	if(len(argv) != 3):
		print("Invalid arguments....")
		exit()

	if(argv[1] == "-h") or (argv[1] == "-H"):
		print("Help : This Application is copy all files whith extension .exe from Demo to Temp")
		exit()

	if(argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage : Application_name Dircetory_Name New_Directory_Name .extension")
		exit()

	DirectoryCopyExt(argv[1],argv[2])

if __name__ == "__main__":
	main()
