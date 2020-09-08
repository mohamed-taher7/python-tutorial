import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr) 
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''

newarr = arr.reshape(2, 3, 2)
'''
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]
'''

print(arr.reshape(2, 4).base)
#The example above returns the original array, so it is a view.

#Unknown Dimension
#this calculates for you the remaining dimension, 2 * 2 * x = 8

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr) 

'''
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
'''
