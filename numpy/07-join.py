#this tutorial is by interpreter
import numpy as np
array2D_1 = array.arange(9).reshape(3,3)
array2D_2 = np.arange(10,19).reshape(3,3)
np.vstack((array2D_1, array2D_2)) #row
#OR
np.concatenate((array2D_1, array2D_2)) #row
#GIVES:
 '''
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [10, 11, 12],
       [13, 14, 15],
       [16, 17, 18]])
'''
  
#transpose:
x = np.ones(4)
y = np.arange(1,5)
print(x)
print(y)
'''
[1. 1. 1. 1.]
[1 2 3 4]
'''

print(np.vstack((x, y)).T)
'''
[[1. 1.]
 [1. 2.]
 [1. 3.]
 [1. 4.]]
'''

np.concatenate((array2D_1, array2D_2, axis = 1)) #column
#OR
np.hstack((array2D_1, array2D_2))
'''
array([[ 0,  1,  2, 10, 11, 12],
       [ 3,  4,  5, 13, 14, 15],
       [ 6,  7,  8, 16, 17, 18]])
'''

# concatenate 3 numpy arrays: row-wise
np.concatenate((array2D_1, array2D_2, array2D_1))
'''
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [10, 11, 12],
       [13, 14, 15],
       [16, 17, 18],
       [ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8]])
'''
