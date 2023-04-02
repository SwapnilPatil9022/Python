# Accept one character from user and convert case of that character.
# 	Input : D	Output : d
# 	tip : A - Z = 65 - 90						# print(chr(ord(No)+32))
#	tip : a - z = 97 - 122

def U_To_L(No):

	for i in No:
		No = chr(ord(i)+32)
		print(No)


def main():
	print("Please enter the Character :")
	str1 = input()

	U_To_L(str1)

if __name__ == "__main__":
	main()