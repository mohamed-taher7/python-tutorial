"""
Data-types with some details
"""
#_____________________________________________Strings_____________________________________________#
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

#_____________________________________________Numbers_____________________________________________#
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



#_____________________________________________Sequences_____________________________________________#
# Sequence Types: 	list, tuple, range
#______________________________________________#
# Lists:
x = ["apple", "banana", "cherry"]   #list: ordered and changeable. Allows duplicate members

thislist = ["apple", "banana", "cherry"]
print(thislist)

# Access Items
# You access the list items by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #output: apple

#Negative Indexing
#Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of Indexes
# the return value will be a new list with the specified items.
#Note: The search will start at index 2 (included) and end at index 5 (not included).
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#first item has index 0

#By leaving out the start value, the range will start at the first item:
print(thislist[:4])
#same with end value

#Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 


# Change Item Value
# To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #output: ['blackcurrant', 'banana', 'cherry']

# Loop Through a List
# You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# List Length
# To determine how many items a list have, use the len() method:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Add Items
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# To add an item at the specified index, use the insert() method:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Remove Item
# There are several methods to remove items from a list:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)  # this will cause an error because "thislist" no longer exists

# The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# The list() Constructor
# It is also possible to use the list() constructor to make a list.
# note the double round-brackets
thislist = list(("apple", "banana", "cherry"))
print(thislist)

#Join Two Lists
#method 1
list3 = list1 + list2
#method 2
for x in list2:
  list1.append(x)

print(list1) 
#method 3
list1.extend(list2)
print(list1) #append list1 to the end of list 2
# List Methods

# Method            Description

# count()           Returns the number of elements with the specified value
# index()           Returns the index of the first element with the specified value
# reverse()         Reverses the order of the list
# sort()            Sorts the list according to it's data-type

#______________________________________________#
 #tuple:  ordered and unchangeable. Allows duplicate members.
 y = ("apple", "banana", "cherry")  #assign
#stuff same as lists:
  #Access Tuple Items
  #Negative Indexing
  #Range of Indexes
  #Loop Through a Tuple
  #Check if Item Exists
  #Tuple Length
#create tuple with one item:
#One item tuple, remember the commma:
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) 


#Change Tuple Values
#you can't!, but convert to list then convert back to tuple:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
 
#tuple method:
thistuple = tuple(("apple", "banana", "cherry"))
#Return the number of times the value 5 appears in the tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(5)) 

#Search for the first occurrence of the value 8, and return its position:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.index(8)) 
 
#______________________________________________#
x = range(6)                        #range(start, stop, step) 
#______________________________________________#
# Mapping Type: 	dict
a = {"name" : "John", "age" : 36}    #dict: unordered, changeable and indexed. No duplicate members.
#______________________________________________#
# Set Types: 	set, frozenset
#set: unordered and unindexed. No duplicate members.
z = {"apple", "banana", "cherry"} 

#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) 

#you cannot change its items, but you can add new items.
 #same as lists:
  #Get the Length of a Set
  #The clear() method 
  #HEREE
  
#To remove an item in a set, use the remove(), or the discard() method.
thisset.remove("banana")
#Note: If the item to remove does not exist, discard() will NOT raise an error.
#pop() will not tell you what item that gets removed.(i.e random deleting)

b = frozenset({"apple", "banana", "cherry"}) #immutable version of a Python set
#______________________________________________#

#_____________________________________________Booleans_____________________________________________#
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


#_____________________________________________Binary Types_____________________________________________#

# Binary Types: 	bytes, bytearray, memoryview
x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))

