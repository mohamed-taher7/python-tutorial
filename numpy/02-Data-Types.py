'''
Below is a list of all data types in NumPy and the characters used to represent them.

    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )
'''
#The NumPy array object has a property called dtype that returns the data type of the array:
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype) #out: int64

#For i, u, f, S and U we can define size as well.

#Create an array with data type 4 bytes integer:

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype) 

#Change data type from float to integer by using 'i' as parameter value:

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype) 

#int to false
arr = np.array([1, 0, 3])
newarr = arr.astype(bool) #[ True False True]


