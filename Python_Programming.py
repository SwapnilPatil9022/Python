

def Display():
	for i in range(1,4):
		for j in range(1,7):
			if j>=6-i:
				print("",end='')
			else:
				print("*",end='')
		print()

def main():

	Display()

if __name__ == "__main__":
	main()





# def Display():
# 	for i in range(1,6):
# 		for j in range(1,6):
# 			if j>=6-i:
# 				print("",end='')
# 			else:
# 				print("*",end='')
# 		print()

# def main():

# 	Display()

# if __name__ == "__main__":
# 	main()









# def Display():
# 	for i in range(1,6):
# 		for j in range(1,6):
# 			if j<=i:
# 				print("*",end='')
# 			else:
# 				print("",end='')
# 		print("\n")

# def main():

# 	Display()

# if __name__ == "__main__":
# 	main()








# from flask import Flask

# from flask import Flask
# from flask_pymongo import PyMongo

# app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
# mongo = PyMongo(app)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# app.run(debug=True)




# d1 = {45:"amit",81:"ajay","age":18,"weight":50}
# for i in d1: 
# 	print(i," : ",d1[i])




# password = "swap"

# counter = 0

# while counter != 3:
# 	counter = counter + 1
# 	pin = (input("Enter the pin : "))
# 	if pin == password:
# 		print("password Mactched....")
# 		break
# 	else:
# 		print("Incorrect pin")
# else:
# 	print("Card Blocked")









# p = 1234
# c = 0
# while c!=3:
# 	c=c+1
# 	pin = int(input("Enter a pin : "))
# 	if pin == p:
# 		print("Transiction succesfull")
# 		break
# 	else:
# 		print("Incorrect pin")
# else:
# 	print("Card Blocked")




# s1 = 33,44,55,66
# l1 = list(s1)
# print(l1)



# A = [11,222,33,4,556,64,6.3,"jay","ganesh"]  
# h1 = A[2:6:1]
# print(A)
# print(h1)


# list
# A = [11,222,33,4,556,64,6.3,"jay","ganesh"]
# for i in A:
# 	print(i)

# A.append("SP")
# print(A)


# A = int(input("enter a number"))

# if(A%2==0):
# 	print("Even")
# else:
# 	print("Odd")






# swaping
# A = int(input("Enter first number : "))
# B = int(input("Enter secound number : "))

# C = 0

# C = A
# A = B
# B = C
# print("A is : ",A,"B is : ",B)




# Itrative statemanets
 

# x = "Swapnil"
# for i in range(5):
# 	print("Hello")  
# 	print("world")




# x = "Swapnil"
# for i in x:
# 	print("Hello")  
# 	print("world")




# x = int(input("Enter first number"))
# y = int(input("Enter secound number"))

# if x>y:
# 	print(x,"is grater")
# elif x<y:
# 	print(x,"is grater1")
# elif x==y:
# 	print("Neigther negative nor positive")






# conditional statemanets

# x = int(input("Enter the number"))
# if x>0:
# 	print(x,"is positive")
# elif x<0:
# 	print(x,"is Negative")
# elif x==0:
# 	print("Neigther negative nor positive")



# x = 5
# if(x>0):
# 	print(x," is positive")
# 	print("Hello")
# print("Bye")






# a = [1,2,3,4,4]
# print(len(a))



# x = 425
# (x)
# print(x)


# r = float(input("Enter a radius : \n"))

# pi = 3.14
# result = pi*r*r
# print("Area of circle is",result)



# x = input() 
  


# import math 
# x = math.factorial(6)
# print(x)

# y = math.gcd(4,6)
# print(y)





# import keyword
# print(keyword.kwlist)
# print("--------------")
# print(len(keyword.kwlist))







# x = 55
# y = 7.1
# z = "H"
# w = 5+7j
# v = 12+6j 

# print(w+v)
# print(type(w))