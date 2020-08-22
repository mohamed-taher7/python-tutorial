# Python Variables

# Creating Variables
x = 5
y = "John"
print(x)
print(y)

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

# Variable Names
#
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores
# Variable names are case-sensitive

# Ouput Variables
x = "awesome"

print("Python is " + x)

x = "Python is "
y = "awesome"
z = x + y
print(z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x + y)
#var names:A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ) (case sensitive and don't start with num)
#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 
#----------------------------------------------#
#Also, use the global keyword if you want to change a global variable inside a function.
