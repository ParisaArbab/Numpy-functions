"""
Author: Parisa Arbab
Date: March 12 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link:https://youtu.be/obihQsqS6Kg

answered this question in the above link:
• Show how you created a, b, and c.
• Explain the results of “a[4,5]” and “a[4]”.
• Why is the result of multiplying a and d different from computing the dot product of a and d?
The multiply() function in NumPy performs element-wise multiplication between two arrays,
while the dot() function calculates the dot product or matrix multiplication between two arrays according to linear algebra rules.

"""
import numpy as np

#Created array a using arange with 100 equally spaced values from 0 to 99
#arrange(start,stop,step )
a = np.arange(0, 100, 1)

# Created array b using arange with 10 equally spaced values from 0 to 90.
b = np.arange(0, 100, 10)

# Created array c using linspace with values from 0 to 10, spaced at 0.1.
#linespace( start, stop, the number of element)
# num = 101 ensures we capture both 0 and 10 with 0.1 increments between them.
c = np.linspace(0, 10, num=101)

# Created array d as a random 10x10 two-dimensional array.
d = np.random.rand(10, 10)

# Reshaped array a to be a 10x10 two-dimensional array.
a = a.reshape(10, 10)

print("a = " , a)
print("b = " , b)

# a[4,5] retrieves the value at the 4th row and 5th column of array a.
print("******Result of a[4,5]:", a[4, 5])

# a[4] retrieves the entire 5th row of array a.
print("******Result of a[4]:", a[4])

# Calculate the sum of all elements in array d
print("******Sum of d:", np.sum(d))

# Find the maximum value in array a
print("******Max of a:", np.max(a))

# Transpose b: flips the matrix over its diagonal. Example:
#B = [[1, 2, 3], [4, 5, 6]]
#Dimention = 2*3

# B^T = [[1, 4],
#        [2, 5],
#        [3, 6]]
#Dimention = 3*2
print("******Transpose of b:", b.T, "\n\n")

# Add arrays a and d element-wise. Example:
#A = [1, 2, 3]
#D = [4, 5, 6]
#A + D = [1+4, 2+5, 3+6] = [5, 7, 9]
print("******Result of adding a and d:\n", np.add(a, d), "\n\n")
print("a = " , a)
print("d = " , d, "\n\n")
# Multiply arrays a and d element-wise multiplies corresponding elements of a and d.
# Example: A * D = [1*4, 2*5, 3*6] = [4, 10, 18]
print("******Result of multiplying a and d:\n", np.multiply(a, d), "\n\n")

# dot: sum of the products of corresponding elements of rows of the first matrix with corresponding elements of columns of the second matrix.
# A = [1, 2, 3]
# D = [4, 5, 6]
# Result = (1*4)+(2*5)+(3*6)= 4+10+18= 32
#dimention of result = number of rows of the first matrix and the number of columns of the second matrix
#results in a new matrix
Result = np.dot(a, d)
print("******Dot product of a and d:\n", Result)


