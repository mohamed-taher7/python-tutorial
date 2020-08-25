"""
Data-types with some details
"""
#______________________Strings___________________________#
# Text Type: 	str
m = "Hello World"

#same as

m = 'Hello World'

# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) #try it

# access elements of the string:

a = "Hello, World!"
print(a[1]) #output: e

#Slicing:
#Get the characters from position 2 (not included) to position 5:
b = "Hello, World!"
print(b[2:5]) #output: llo

# Negative Indexing
#Get the characters from position 5 to position 1 (not included), starting the count from the end of the string:

b = "Hello, World!"
print(b[-5:-2]) #output: orl

# String Length
#To get the length of a string

a = "Hello, World!"
print(len(a)) #output: 13

# String Methods:
  #strip()
    a = " Hello, World! "
    print(a.strip()) # returns "Hello, World!" 
  #lower()
    a = "Hello, World!"
    print(a.lower()) # returns "hello, world!" 
  #upper() : same as above but makes all upper-case
  #replace()
    a = "Hello, World!"
    print(a.replace("H", "J"))
  #split():  splits a string into a list.
    a = "Hello, World!"
    print(a.split(",")) # returns ['Hello', ' World!'] 
    print(a.split())    # returns ['Hello,', 'World!']
  #more methods here: https://www.w3schools.com/python/python_ref_string.asp
# Check String

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) #output: False

# String Concatenation

a = "Hello"
b = "World"
c = a + " " + b
print(c) #output: Hello World

# String Format
#Use the format() method to insert numbers into strings:

#EX1
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#EX2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(itemno , quantity, price)) #output: I want to pay 49.95 dollars for 567 pieces of item 3.

# Escape characters
print("We are the so-called \"Vikings\" from the north.") #output: We are the so-called "Vikings" from the north.
"""
\" 	Double Quote 	
\' 	Single Quote 	
\\ 	Backslash 	
\n 	New Line 	
\r 	Carriage Return 	
\t 	Tab 	
\b 	Backspace 	
\f 	Form Feed 	
\ooo 	Octal value 	
\xhh 	Hex value
"""

#convert from int/float/comlex to string:
a = str(x)

#______________________Numbers____________________________#
# Numeric Types: 	int, float, complex
x, y, z = 1, 35656222554887711, -3255522      # int:  whole number, positive or negative, without decimals, of unlimited length.
a, b, c = 2.8, -35.59, -87.7e100 # float: positive or negative, containing one or more decimals.
z = 3-51j      # complex

#Type Conversion

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y) #1.0 will be 1

#convert from int to complex:
c = complex(x, l) #l is img part if exist
# Note: You cannot convert complex numbers into another number type.
"""
Note:When converting from a string, the string must not contain whitespace around the central + or - operator.
For example, complex('1+2j') is fine, 
but complex('1 + 2j') raises ValueError.
"""

# to make random num
import random

print(random.randrange(1, 10)) 

"""
 Operator              Name                Example
   +                 Addition               x + y
   -                 Subtraction            x - y
   *                 Multiplication         x * y
   /                 Division               x / y
   %                 Modulus                x % y
  **                 Exponentiation         x ** y
  //                 Floor division         x // y
"""



#______________________Sequences____________________________#
# Sequence Types: 	list, tuple, range
x = ["apple", "banana", "cherry"]   #list: ordered and changeable. Allows duplicate members
y = ("apple", "banana", "cherry")   #tuple:  ordered and unchangeable. Allows duplicate members.
x = range(6)                        #range(start, stop, step) 

# Mapping Type: 	dict
a = {"name" : "John", "age" : 36}    #dict: unordered, changeable and indexed. No duplicate members.

# Set Types: 	set, frozenset
z = {"apple", "banana", "cherry"}   #set: unordered and unindexed. No duplicate members.
b = frozenset({"apple", "banana", "cherry"}) #immutable version of a Python set

#______________________Booleans____________________________#
# Boolean Type: 	bool
m = True
l = False
"""
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""
bool("mediate") #output: True
#note: Functions can Return a Boolean
"""
Operators for booleans

== 	Equal 	x == y 	
!= 	Not equal 	x != y 	
> 	Greater than 	x > y 	
< 	Less than 	x < y 	
>= 	Greater than or equal to 	x >= y 	
<= 	Less than or equal to 	x <= y

and  	  Returns True if both statements are true 	x < 5 and  x < 10 	
or 	    Returns True if one of the statements is true 	x < 5 or x < 4 	
not 	  Reverse the result, returns False if the result is true 	not(x < 5 and x < 10) 	
is  	  Returns True if both variables are the same object 	x is y 	
is not  Returns True if both variables are not the same object
in  	  Returns True if a sequence with the specified value is present in the object 	x in y 	
not in 	Returns True if a sequence with the specified value is not present in the object 	x not in y 	
"""

#EX
print(6>=9) #False

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list


#______________________Binary Types____________________________#

# Binary Types: 	bytes, bytearray, memoryview
x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))

