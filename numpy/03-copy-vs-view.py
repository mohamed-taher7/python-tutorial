'''
The copy owns the data and any changes made to the copy will not affect original array
The view does not own the data and any changes made to the view will affect the original array
'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy() #new array


arr = np.array([1, 2, 3, 4, 5])
x = arr.view() #image of original
x[0] = 42

print(arr)
print(x)

#Print the value of the base attribute to check if an array owns it's data or not:
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base) #out: None
print(y.base) #out: [1, 2, 3, 4, 5]
