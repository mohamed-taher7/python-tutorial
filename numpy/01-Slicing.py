#the slicing is like this [start:end:step]
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5]) #Slice elements from index 4 to the end of the array:
print(arr[4:])  #Slice elements from the beginning to index 4 (not included):

#Negative Slicing:
print(arr[-3:-1]) #out: [5, 6]

#

print(arr[1:5:2]) #out: [2, 5]

print(arr[::2]) #out: [1, 3, 5, 7]

#From the second element, slice elements from index 1 to index 4 (not included):
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) 

#From both elements, return index 2:
print(arr[0:2, 2]) 

#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(arr[0:2, 1:4]) 
