from sys import*
import os
import hashlib

def hashfile(path, blocksize = 1024):
	afile = open(path, 'rb')
	hasher = hashlib.md5()
	buf = afile.read(blocksize)

	while len(buf) > 0:
		hasher.update(buf)
		buf = afile.read(blocksize)

	afile.close()

	return hasher.hexdigest()

def FindDuplicate(path):
	flag = os.path.abspath(path)

	if flag == False:
		path = os.path.isdir(path)

	exists = os.path.isdir(path)

	dups = {}

	if exists:
		for dirName, subdirs, fileList in os.walk(path):
			for filen in fileList:
				path = os.path.join(dirName, filen)
				file_hash = hashfile(path)
				if file_hash in dups:
					dups[file_hash].append(path)
				else:
					dups[file_hash] = [path]

		return dups
	else:
		print("Invalid Path")

def PrintDuplicate(dict1):
	results = list(filter(lambda x : len(x) > 1, dict1.values()))

	if len(results) > 0:
		print("Duplicate Found : ")

		print("The following files are identical.")

		icnt = 0;
		for result in results:
			for subresult in result:
				icnt+=1
				if icnt >= 2:
					print('\t\t%s' % subresult)

	else:
		print("No duplicate file found.")

def main():
	print("-------Application of Search Duplicate files by Swapnil Patil---------")

	print("Application name : "+argv[0])

	if(len(argv) != 2):
		print("Invalid argument..")
		exit()

	if(argv[1] == "-h") or (argv[1] == "-H"):
		print("Help : Accept directory and display checksum of all files.")
		exit()

	if(argv[1] == "-u") or (argv[1] == "-U"):
		print("Usage : Application_Name directory_Name")
		exit()

	try:
		arr = {}
		arr = FindDuplicate(argv[1])
		PrintDuplicate(arr)

	except ValueError:
		print("Error : Invalid datatype of input")

	except Exception as E:
		print("Error : Invalid input",E)

if __name__ == "__main__":
	main()
