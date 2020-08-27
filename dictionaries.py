#assign
thisdict = {
    "key" : "value"
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
#or
thisdict = dict(brand="Ford", model="Mustang", year=1964)

# Accessing Items
#Get the value of the "model" key:

x = thisdict["model"]
x = thisdict.get("model") #output: Mustang

# Change Values

thisdict["year"] = 2018

# Loop Through a Dictionary
#
# Print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)

# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

# Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
    print(x, y)

# Dictionary Length
#
# To determine how many items (key-value pairs) a dictionary have, use the len method.
print( len(thisdict) )

# Adding Items
#
# Adding an item to the dictionary is done by using a new index key and
thisdict["color"] = "red"
print(thisdict)

# Removing Items

# The del keyword removes the item with the specified key name:
del thisdict["model"]


# The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:
del thisdict["model"]

# The del keyword can also delete the dictionary completely:
del thisdict

# The clear() keyword empties the dictionary:
thisdict.clear()


# Dictionary Methods
#
# Python has a set of built-in methods that you can use on dictionaries.
#
# Method                Description
# clear()               Removes all the elements from the dictionary
# copy()                Returns a copy of the dictionary
# fromkeys()            Returns a dictionary with the specified keys and values
# get()                 Returns the value of the specified key
# items()               Returns a list containing the a tuple for each key value pair
# keys()                Returns a list containing the dictionary's keys
# pop()                 Removes the element with the specified key
# popitem()             Removes the last inserted key-value pair
# setdefault()          Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()              Updates the dictionary with the specified key-value pairs
# values()              Returns a list of all the values in the dictionary
