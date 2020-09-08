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

