# Accept one character from user and convert case of that character.
#	Input : a 	Output : A
# 	tip : A - Z = 65 - 90						# print(chr(ord(No)-32))
#	tip : a - z = 97 - 122

def L_To_U(No):
	
	for i in No:
		No = chr(ord(i)-32)
		print(No)


def main():
	print("Please enter the Character :")
	str1 = input()

	L_To_U(str1)

if __name__ == "__main__":
	main()