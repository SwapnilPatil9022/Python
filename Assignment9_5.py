"""
  5 . Accept file name and one string from user and return the frequency of that string from file.

  	Input : Demo.txt	Marvellous
  	Search "Marvellous" in Demo.txt
"""

import os

def Freq_str(fname):
	if (os.path.exists(fname)):
		fd = open(fname,"r")
		Read = fd.read()
		print(Read)

		d1 = {}
		Data = input("Enter the string :\n")
		
		for line in fname:
			words = line.split()
			for word in words:
				if word in d1:
					d1[word] = d1[word] + 1
				else:
					d1[word] = 1
		print(words)

	else:
		print("File not found.")

def main():
	print("-----Inside Main method-----")
	print("----------------------------")

	File = input("Enter the File name : \n")
	print("----------------------------")

	Freq_str(File)

if __name__ == "__main__":
	main()

