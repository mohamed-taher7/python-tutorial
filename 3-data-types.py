print("data types by examples")
"""
Text Type: 	str
m = "Hello World"

Numeric Types: 	int, float, complex
x = 1       # int
y = 2.8     # float
z = 1j      # complex
---------
#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)
Note: You cannot convert complex numbers into another number type.
to make random num
import random

print(random.randrange(1, 10)) 
-----------------
Sequence Types: 	list, tuple, range
x = ["apple", "banana", "cherry"]   #list: ordered and changeable. Allows duplicate members
y = ("apple", "banana", "cherry")   #tuple:  ordered and unchangeable. Allows duplicate members.
x = range(6)                        #range(start, stop, step) 
Mapping Type: 	dict
a = {"name" : "John", "age" : 36}    #dict: unordered, changeable and indexed. No duplicate members.

Set Types: 	set, frozenset
z = {"apple", "banana", "cherry"}   #set: unordered and unindexed. No duplicate members.
b = frozenset({"apple", "banana", "cherry"}) #immutable version of a Python set

Boolean Type: 	bool
m = True
l = False

Binary Types: 	bytes, bytearray, memoryview
x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))
"""
