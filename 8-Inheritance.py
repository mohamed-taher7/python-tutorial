#__________________________________Inheritance________________________________#

#Inheritance allows us to define a class that inherits all the methods and properties from another class.

"""
Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
"""

#Parent Class(Any class can be a parent):

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() 

#Create a class named Student, which will inherit the properties and methods from the Person class:
#send the parent class as a parameter to inherit

 class Student(Person):
  pass 

x = Student("Mike", "Olsen")
x.printname() 
"""
Note: The __init__() function is called automatically every time the class is being used to create a new object.

When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

"""
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) 
 
 #or with the super() Function
 
 class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) 
 
