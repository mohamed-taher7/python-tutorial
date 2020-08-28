
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

