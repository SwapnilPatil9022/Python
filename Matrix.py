import numpy as np

# Create a 3x3 matrix filled with zeros
matrix_zeros = np.zeros((3, 3))
print("Matrix filled with zeros:")
print(matrix_zeros)

# Create a 3x3 matrix filled with ones
matrix_ones = np.ones((3, 3))
print("\nMatrix filled with ones:")
print(matrix_ones)

# Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("\nIdentity Matrix:")
print(identity_matrix)

# Create a 2x3 matrix with custom values
custom_matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\nCustom Matrix:")
print(custom_matrix)

# Matrix addition
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_sum = matrix1 + matrix2
print("\nMatrix Addition:")
print(matrix_sum)

# Matrix multiplication
matrix3 = np.array([[1, 2], [3, 4]])
matrix4 = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix3, matrix4)
print("\nMatrix Multiplication:")
print(matrix_product)

# Transpose of a matrix
matrix_transpose = np.transpose(matrix_product)
print("\nTranspose of Matrix:")
print(matrix_transpose)

# Accessing elements of a matrix
print("\nElement at (1,1):", matrix3[1, 1])

# Slicing a matrix
print("\nSliced Matrix:")
print(matrix3[:, 1])  # Second column

# Matrix operations
print("\nMatrix Operations:")
print("Maximum element:", np.max(matrix3))
print("Minimum element:", np.min(matrix3))
print("Sum of all elements:", np.sum(matrix3))
print("Product of all elements:", np.prod(matrix3))
