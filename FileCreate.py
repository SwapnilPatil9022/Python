def CreateFile(FileName):
	fd = open(FileName,"w")

def main():
	print("Enter the file name to create")
	Name = input()

	CreateFile(Name)

if __name__ == "__main__":
	main()
