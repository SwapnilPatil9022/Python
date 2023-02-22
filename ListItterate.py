# Data : Heterogeneous
# Ordered : Yes
# Indexed : Yes
# Mutable : Yes
# Duplicates : Yes

Data = [11,21,51,101]
print("_____________________________")

print("Output using for")
for no in Data:
    print(no, end = " ")
print("\n_____________________________")

print("Output using for with index")
for i in range(0,len(Data)):
    print(Data[i], end = " ")
print("\n_____________________________")

print("Output using while with index")
i = 0
while(i < len(Data)):
    print(Data[i], end = " ")
    i+=1        # i = i + 1
print("\n_____________________________")