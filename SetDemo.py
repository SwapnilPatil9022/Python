print("Demonstration of Set")

# Data : Hetrogeneous
# Orderd : No
# Indexed : No
# Mutable : Yes
# Duplicates : No

data = {11,21,51,101,21,11}                      # Duplicates
data1 = {11, 90.80, True, "Hello"}         #Hetrogeneous

print("First Set data : ",data)
print("Length of data : ",len(data))
print("Data is Hetrogeneous : ",data1)
print("Data is unorderd : ",data1)
#print("Data is index 2 : ",data[2])
print("Data with Unique elements : ",data)

print("Set is mutable")
#insert element in set
data.add(211)
print("Data after insertion : ",data)

# Remove element
data.remove(211)
print("Data after removel : ",data)
                                        # OR
data.discard(201)
print("Data after Discard : ",data)

