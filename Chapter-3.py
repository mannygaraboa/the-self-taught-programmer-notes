# ===========================================================================
# Chapter 3: Introduction to Programming
# ===========================================================================


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

x = 14.0 / 3.0      # 4.6666666666666667
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

# Exponentiation
expo = 3 ** 4
print (expo)

#PEMDAS
x = 15 - 3 + 2
print(x)

# ===========================================================================
# - Comparison Operators - Pg. 29
# ===========================================================================

bool1 = 1 != 1
print (bool1)

# ===========================================================================
# - Logical Operators - Pg. 32
# ===========================================================================

logiOps = 1 == 1 and 10 != 2 and  2 < 3
print (logiOps)

# Placing the keyword "not" in front of an expression 
# will change the result of the evaluation to 
# the opposite of what it would have otherwise evaluated to.

logiOps2 = not 1 == 2
print (logiOps2)

# ===========================================================================
# - Conditional Statements - Pg. 35
# ===========================================================================

# Keywords "if", "elif", & "else" are used in conditional statements

home = "America"
if home == "America" :
    print ("Hello, America!")
else:
    print ("Hello, World!")

x = 2
if x == 2:
    print ("The number is 2.")
if x % 2 == 0:
    print ("The number is even.")
if x % 2 != 0:
    print ("The number is odd")

# Nesting

x = 10
y = 11

if x == 10:
    if y == 11:
        print (x + y)

# elif-statements

x = 100
if x == 10:
    print ("10!")
elif x == 20:
    print ("20!")
else:
    print ("I don't know!")

if x == 100:
    print ("x is 100!")

if x % 2 == 0:
    print ("x is even!")
else:
    print ("x is odd!")

# ===========================================================================
# - Statements - Pg. 40
# ===========================================================================

# Compound Statements are madeup of 1 or more clauses.

# Clause: consists of two or more lines of code:
    # header: a line of code in a clause that contains a keyword, followed by a colon and a sequence of one or more lines ofindented code.

    # suite: just a line of code in a clause.

# ===========================================================================
# - Challenges - Pg. 44
# ===========================================================================

# 1.) Print three different strings

print ("It's Sunday.")
print ("Daylight Savings!!")
print ("More Sun woo!!")

# 2.) Write a program that prints a message if a variable is less than 10
# and different message if the variable is greater than or equal to 10.

num = 11
if num < 10:
    print("num is less than 10")
else:
    print("num is greater than or equal to 10")

# 3.) Write a program that prints a message if a variable is less than or equal to 10,
# another message if the variable is greater than 10 but less than or equal to 25,
# & another message if the variable is greater than 25.

num2 = 26
if num2 <= 10:
    print ("num2 is less than or equal to 10")
elif num2 > 10 and num2 <= 25:
    print ("num2 is greater than 10 & less than or equal to 25")
else:
    print ("num2 is greater than 25")

# 4.) Create a program that divides two variables and prints the remainder

x = 43
y = 9
num3 = x % y
print (num3)

# 5.) Create a program that takes two variables, divides them, and prints the quotient.

x = 23
y = 5
num4 = x / y
print (num4)

# 6.) Write a program with a variable "age" assigned to an integer 
# that prints different strings depending on what integer "age" is.

age = 21
if age <= 17:
    print ("Minor")
elif age >= 18 and age < 21:
    print ("Can't drink yet")
else:
    print ("Cheers!")
