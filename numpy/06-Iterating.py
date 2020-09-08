import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x) 
'''
[1 2 3]
[4 5 6] 
'''
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y) 
'''
1
2
3
4
5
6
'''
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
#same as above


#Iterating Array With Different Data Types:
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']): 
#NumPy does not change the data type of the element in-place (where the element is in array) 
#so it needs some other space to perform this action, that extra space is called buffer
  print(x) 
  
#Iterating With Different Step Size:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x) 
'''
1
3
5
7
'''
>>>>>>>>>>>>>>>>>>>>>>>continue
