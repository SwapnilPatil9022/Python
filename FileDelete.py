import os

def Delete_File(FileName):
	if(os.path.exists(FileName)):
		os.remove(FileName)
	else:
		print("There is no such file")
		

def main():
	print("Enter the file name to Delete")
	Name = input()

	Delete_File(Name)

if __name__ == "__main__":
	main()