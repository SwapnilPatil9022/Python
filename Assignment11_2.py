"""
  1.Design automation script which accept directory name and write names of duplicate files from
	that directory into log file named as Log.txt. Log.txt file should be created into current directory.

  	Usage : DirectoryChecksum.py  "Demo"

  	Demo is name of directory.
"""
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

def DirectoryChecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')

        NewName = "Log1.txt"
        fd = open(NewName,"a")
        fd.write(file_hash)
        
    else:
        print("Invalid Path")

def main():
    print("-------Application of checksum files---------")

    print("Application name : "+argv[0])

    if(len(argv) != 2):
        print("Invalid argument..")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : Accept directory and display checksum of all files.")

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_Name directory_Name")

    DirectoryChecksum(argv[1])

if __name__ == "__main__":
    main()
