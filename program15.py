# Accept one character from user and check whether that character is vowel (a,e,i,o,u) or not.
#	Input : E 	Output : True
#`	Input : d 	Output : False

def Chk(No):

	Cnt = 0
	list1 = ["a","e","i","o","u"]

	for i in No:
		if i in list1:
			Cnt = Cnt + 1
			return True
		else:
			return False

def main():
	print("Please enter the Character :")
	str1 = input()

	Ret = Chk(str1)

	if (Ret == True):
		print("True")
	else:
		print("False")

if __name__ == "__main__":
	main()