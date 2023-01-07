from sys import*
import os
import hashlib
import time

def DeleteFiles(dict1):
	result = list(filter(lambda x: len(x) > 1, dict1.values()))

	icnt = 0;

	if len(result) > 0:
		for result in results:
			for subresult in result:
				icnt+=1
				if icnt >= 2:
					os.remove(subresult)
			icnt = 0
	else:
		print("No duplicate files found.")

def hashfile(path, blocksize = 1024):
	afile = open(path,'rb')
	hasher = hashlib.md5()
	buf = afile.read(blocksize)

	while len(buf) > 0:
		hasher.update(buf)
		buf = afile.read(blocksize)
	afile.close()

	return hasher.hexdigest()

def FindDup(path):
	flag == os.path.isabs(path)

	if flag == False:
		path = os.path.abspath(path)

	exists = os.path.isdir(path)

	dups = {}

	if exists:
		for dirName,subdirs,fileList in os.walk(path):
			print("Current folder is : "+dirName)
			for file in fileList:
				path = os.path.join(dirName, filen)
				file_hash = hashfile(path)

				if file_hash in dups:
					dups[file_hash].append(path)
				else:
					dups[file_hash] = [path]

			return dups
		else:
			print("Invalid Path")

def PrintResults(dict1):
	result = list(filter(lambda x: len(x)>1,dict1.values()))

	if len(result) > 0:
		print("Duplicates Found :")
		print("The following files are duplicates.")
		for result in results:
			for subresult in result:
				print('\t\t%s'% subresult)
	else:
				print("No Duplicate file found.")

def main():
	print("-----Directory Watcher by Swapnil Patil-----")

	print("Application name : "+argv[0])

	if (len(argv)!= 2):
		print("Error : Invalid number of argument")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("This Script is used to traverse specific directory and display size of files.")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("usage : Application Absolutepath_of_Directory Extension.")
		exit()

	try:
		arr = {}
		startTime = time.time()
		arr = FindDup(argv[1])
		PrintResults(arr)
		DeleteFiles(arr)
		endTime = time.time

		print('Took %s secound to evaluate.'%(endTime - startTime))

	except ValueError:
		print("Error : Invalid datatype of input")

	except Exception as E:
		print("Error : Invalid input",E)

if __name__ == "__main__":
	main()