print("data types by examples")
#__________________________________________________#
# Text Type: 	str
m = "Hello World"
#__________________________________________________#
# Numeric Types: 	int, float, complex
x, y, z = 1, 35656222554887711, -3255522      # int:  whole number, positive or negative, without decimals, of unlimited length.
a, b, c = 2.8, -35.59, -87.7e100 # float: positive or negative, containing one or more decimals.
z = 3-51j      # complex

#Type Conversion

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)
# Note: You cannot convert complex numbers into another number type.

# to make random num
import random

print(random.randrange(1, 10)) 
#__________________________________________________#
# Sequence Types: 	list, tuple, range
x = ["apple", "banana", "cherry"]   #list: ordered and changeable. Allows duplicate members
y = ("apple", "banana", "cherry")   #tuple:  ordered and unchangeable. Allows duplicate members.
x = range(6)                        #range(start, stop, step) 

# Mapping Type: 	dict
a = {"name" : "John", "age" : 36}    #dict: unordered, changeable and indexed. No duplicate members.

# Set Types: 	set, frozenset
z = {"apple", "banana", "cherry"}   #set: unordered and unindexed. No duplicate members.
b = frozenset({"apple", "banana", "cherry"}) #immutable version of a Python set

# Boolean Type: 	bool
m = True
l = False

# Binary Types: 	bytes, bytearray, memoryview
x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))

