#____________________________________inheritance_______________________________#

"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class(Any class can be a parent class): class being inherited from, also called base class.
Child class: class inherits from another class, also called derived class.
"""
class Person:
  def __init__(lol, fname, lname):
    lol.firstname = fname #it's name is lol to diffrentiate between it and the next "self" only
    lol.lastname = lname
    print ("the __init__ func. is run immeadiately after class object is created(whether it ran or not)")

  def printname(self):
    print(self.firstname +" "+ self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe") #class object is created
#try above with this command
#x.printname()

#child class(by passing class as variable):
class Student(Person): #Now the Student class has the same properties and methods as the Person class
  pass
x = Student("Mike", "Olsen")
x.printname()

#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

class Student(Person):
  def __init__(self, fname, lname): 
    #add properties etc. 


#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) 
#OR
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) 

#Add a property called graduationyear to the Student class:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
x = Student("Mike", "Olsen", 2019) 

#Add a method called welcome to the Student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 
