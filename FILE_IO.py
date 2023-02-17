"""
	Cosider below application which demonstrates file IO
"""
fd = ("Marvellous.txt",'r')

print("Information about file : ",fd)

print("Contents of Whole file")
print(fd.read())

print("Reading single line from file")
print(fd.readline())

print("Current file position is",fd.tell())

fd.seek(0)

print("Contents of Whole file")
print(fd.read())

fd.close()

fd = open("Marvellous.txt",'a+r')

fd.write("Python : Automation and Machine Lerning\n")
fd.write("Angular : Web Development\n")

fd.seek(0)

print(fd.read())

fd.close()