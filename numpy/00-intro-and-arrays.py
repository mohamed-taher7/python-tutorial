"""
NumPy: open source python library used for working with arrays,  linear algebra, fourier transform, and matrices.
NumPy aims to provide an array object that is up to 50x faster that traditional Python lists.
Also it is optimized to work with latest CPU architectures.
is written partially in Python, but most of the parts that require fast computation are written in C or C++.
"""
#install it: pip install numpy
import numpy as np

#NumPy Creating Arrays:
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr)) #output: <class 'numpy.ndarray'>

#Dimensions in arrays(nested arrays):
0_dimensional = np.array(42)
1_dimensional = np.array([1, 2, 3, 4, 5])
2_dimensional = np.array([[1, 2, 3], [4, 5, 6]])
3_dimensional = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#Check Number of Dimensions?:
print(0_dimensional.ndim) #output: 0
#... and so on


#you can define the number of dimensions by using the ndmin argument:
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

#Array Indexing:

#Get third and fourth elements from the following array and add them:
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3]) 

#Access 2-D Arrays:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st dim: ', arr[0, 1]) 

#Negative Indexing:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])  #output: 10
