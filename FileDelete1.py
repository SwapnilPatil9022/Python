import os

def Delete_File(FileName):
	if(os.path.exists(FileName)):
		size = os.path.getsize(FileName)
		if(size == 0):
			os.remove(FileName)
		else:
			print("Are you sure to delete the the file? Y/N")
			option = input()
			if(option == "Y") or (option == "y"):
				os.remove(FileName)
			else:
				print("File deletion process stoped.")
		
	else:
		print("There is no such file")

def main():
	print("Enter the file name to Delete")
	Name = input()

	Delete_File(Name)

if __name__ == "__main__":
	main()