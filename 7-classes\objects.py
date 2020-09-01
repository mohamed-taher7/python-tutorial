"""
https://www.youtube.com/watch?v=8yjkWGRlUmY
#___________________________________________Classes and Objects___________________________________________#

"""
 Python is an object oriented programming language.
 Almost everything in Python is an object, with its properties and methods.
 A Class is like an object constructor, or a "blueprint" for creating objects.
"""


# To create a class, use the keyword class:
class MyClass:
    x = 5

#Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x) 

"""
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age) 

#Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() 

"""
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
"""

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc() 

#Set the age of p1 to 40:
p1.age = 40 

#Delete Object Properties
del p1.age

#Delete Objects
del p1


#class definitions can be empty by pass:

class Person:
  pass
