import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x) 
'''
(array([3, 5, 6],)
'''
#Which means that the value 4 is present at index 3, 5, and 6.

#find where the even values:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x) #output is  array index of even

#searchsorted():
#This method is assumed to be used on sorted arrays.

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x) #out: 1

#arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x) 
