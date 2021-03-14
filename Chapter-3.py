# print "Hello, World!" 5  times & "montyPython" 3 times.
for i in range(5) :
    print ("Hello, World!")

for i in range(3) :
    print ("montyPython")

# length of a diagonal 
import math
l = 4
w = 10
d = math.sqrt(1**2 + w**2)
print d

# The slash allows to put 
# ("""This is a really really really really long line of code.""") 
# & print on separate lines (otherwise not allowed)

print\
    ("""This is a really really really really long line of code.""")

# ===========================================================================
# - Constants & Variables - Pg. 20
# ===========================================================================

x = 10
y = 10 
z = x + y
print (z)
a = x - y
print (a)

my_string = "Hello World."
print (my_string)


# ===========================================================================
# - Errors & Exceptions - Pg. 25
# ===========================================================================

# Exception: Any error that is not a syntax error

# This code has an error (ZeroDivisionError: division by zero)
# x = 10 / 0
# print (x)

# This code has an error (IndentationError: unexpected indent)
# y = 2
#   x = 1

# ===========================================================================
# - Arithmetic Operators - Pg. 26
# ===========================================================================

x = 13 / 5
y = 13 // 5
z = 13 % 5
print (x)
print (y)
print (z)

# even
evenNum = 12 % 2
print (evenNum)

# odd
oddNum = 11 % 2
print (oddNum)
