from sys import*
import os
import hashlib

def hashfile(path, blocksize = 1024):
	afile = open(path,'rb')
	hasher = hashlib.md5()
	buf = afile.read(blocksize)
	while len(buf) > 0:
		hasher.update(buf)
		buf = afile.read(blocksize)
	afile.close()
	return hasher.hexdigest()

def FindChecksum(path):
	flag == os.path.isabs(path)
	if flag == False:
		path = os.path.abspath(path)

	exists = os.path.isdir(path)

	if exists:
		for dirName,subdirs,fileList in os.walk(path):
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
		DirectoryWatcher(argv[1])

	except ValueError:
		print("Error : Invalid datatype of input")

	except:
		print("Error : Invalid input")

if __name__ == "__main__":
	main()