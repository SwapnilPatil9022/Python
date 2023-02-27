import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

fruit = ['Apple','Orange','Mango','Guava']
quantity = [67,34,100,29]

plt.pie(quantity,labels=fruit,autopct="%0.1f%%'")
plt.show()

x = [10,20,30,40,50,60,70,80,90]
a = [8,1,7,2,0,3,7,3,2]
b = [7,2,5,6,9,1,4,5,3]

data = list([x,a,b])

plt.boxplot(data)
plt.show()

plt.scatter(x,a,marker="*",c="g",s=100)
plt.scatter(x,b,marker=".",c="r",s=200)
plt.show()





















"""
# Bar plot

student = {"Bob":87,"Matt":56,"Sam":27}


names = list(student.keys())
values = list(student.values())

plt.barh(names,values,color="b")
plt.title("Bar plot")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
"""









"""
# Bar plot

plt.bar(names,values)
plt.title("Bar Plot")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.grid(True)
plt.show()


plt.bar(names,values)
plt.show()


"""






"""
x = np.arange(1,11)
x

y1 = 2*x
y2 = 3*x

plt.plot(x,y1,color="b",linestyle=":",linewidth=3)
plt.plot(x,y2,color="r",linestyle="-",linewidth=3)
plt.title("First line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()

print(x)
print("------------------------------------------")

x = np.arange(1,11)
y1 = 2*x
y2 = 3*x

plt.subplot(1,2,1)
plt.plot(x,y1,color="g",linestyle=":",linewidth=2)

plt.subplot(1,2,2)
plt.plot(x,y2,color="r",linestyle=":",linewidth=2)

plt.show()

print("---------------------------------------")

plt.subplot(1,5,1)
plt.plot(x,y1,color="yellow")

plt.subplot(2,9,2)
plt.plot(x,y1,color="orange")

plt.show()
"""