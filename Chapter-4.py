# ===========================================================================
# Chapter 4: Functions
# ===========================================================================

# ===========================================================================
# - Functions - Pg. 47
# ===========================================================================

# Calling a funcition means giving the function the input 
# it needs to execute its instructions and return an output.

# [function_name] ([parameters_separated_by_commas])

def f(x):
  return x * 2

print (f(4))

def func1(x):
  return x + 1

z = func1(4)

if z == 5:
  print("z is 5")
else:
  print ("z is not 5")

# Function without parameters
def func2():
  return 1 + 1

result1 = func2()
print result1

# Function with more than 1 parameter
def func3(x, y, z):
  return x + y + z

sum1 = func3(3, 5, 7)
print sum1

# Function without a return statement --> returns "None"
# def func4():
#   zyx = 2 + 2

# result2 = func4()
# print result2

# ===========================================================================
# - Built-In Functions - Pg. 51
# ===========================================================================

# "len" => returns the length of an object
length1 = len("Monty")
print (length1)

# "str" takes an object & returns a new object with a "str" data type
string1 = str(100)
print (string1)

# "int" function returns an integer object
int1 = int("1")
print (int1)

# "float" function returns a floating point number object
float1 = float(100)
print (float1)

int1 = int("110")
int2 = int(20.54)
print (int1)
print (int2)

float1 = float("16.4")
float2 = float(99)
print (float1)
print (float2)

# "input" collects information from the person using the program.
# Takes a string as a parameter.

age = input("Enter your age: ")
int_age = int(age)
if int_age < 21:
  print("You are young!")
else:
  print("Wow, you are old!")


# ===========================================================================
# - Reusing Functions - Pg. 54
# ===========================================================================

# Function that can be called whenever
def even_odd():
  n = input("type a number: ")
  n = int(n)
  if n % 2 == 0:
    print ("n is even")
  else:
    print ("n is odd")

even_odd()


# ===========================================================================
# - Required & Optional Parameters - Pg. 56
# ===========================================================================

# Optional parameters: ["function_name"] (["parameter_name"] = ["parameter_value"])

def op_Param(x=2):
  return x**x

print(op_Param())    # >> 4
print(op_Param(4))   # >> 256

# Can define a function that has both required & optional parameters.
# Define all the required parameters first.

def add_it(x, y = 10):
  return x + y

result = add_it(2)   # >> 12
print result


# ===========================================================================
# - Scope - Pg. 57
# ===========================================================================

# Variables have an important property call scope.
# When you define a variable, its scope refers to what part of your program 
# can read & write to it.

# Global Scope: It can be read or written to from anywhere in your program.
# >> Global Variable.

# Local Scope: Your program can only read or write to it in the function (or class)
# the variable was defined within.

globe1 = 1
globe2 = 2
globe3 = 3

def globe():
  print(globe1)
  print(globe2)
  print(globe3)

globe()

def local():
  local1 = 10
  local2 = 20
  local3 = 30
  print(local1)
  print(local2)
  print(local3)

local()

# Writing to a global variable inside of a local scope takes an extra step.
# Use "global" keyword, followed by the variable you want to change.

control = 100

def change_control():
  global control
  control += 1
  print (control)

change_control() # >> 101


# ===========================================================================
# - Exception Handling - Pg. 61
# ===========================================================================

# Exception Handling: Allows you to test for error conditions, "catch" exceptions
# if they occur, and decide how to proceed.

# Keywords "try" & "except"
  # "try": clause contains the error that could occur.
  # "except": clause contains code that will only execute if the exception in your 
  #           "try" clause occurs.

# Each exception in Python is an object

def two_nums1():
  a = input("type a number: ")
  b = input("type another: ")
  a  = int(a)
  b = int(b)
  try:
    print (a / b)
  except ZeroDivisionError:
    print ("b cannot be zero.")

two_nums1()

# A "ValueError" occurs if you give the built-in functions "int", "string", 
# or "float" bad input

# "except" statement can have 2 exceptions by adding parentheses around "except" 
# & separating the exceptions with a comma.

def two_nums2():
  try:
    a = input("type a number: ")
    b = input("type another: ")
    a = int(a)
    b = int(b)
    print (a / b)
  except (ZeroDivisionError, ValueError):
    print ("Invalid input")

two_nums2()


# ===========================================================================
# - Docstrings - Pg. 64
# ===========================================================================

# Docstrings: explain what the function does, and document what kinds of parameters
#             it needs.

def add(x, y):
  """
  Returns x + y.
  :param x: int.
  :param y: int.
  :return: int sum of x and y.
  """
  return x + y


# ===========================================================================
# - Challenges - Pg. 66
# ===========================================================================

# 1.) Write a function that takes a number as an input and returns that number squared.

def square_num():
  """
  Returns squared input of the user.
  :input x: int.
  :print: square of input x.
  """
  x = input("Give number to square: ")
  x = int(x)
  print(x**2)

square_num()

# 2.) Create a function that accepts a string as a parameter and prints it.

def stringParam(string):
  """
  Returns string within parameter.
  :param string: string.
  :print: string.
  """
  print (string)

stringParam("Jello World!")

# 3.) Write a function that takes three required parameters two optional parameters.

def fruitBasket(apple, banana, orange, grape = 2, mango = 3):
  """
  Returns 5 integers, last 2 are optional parameters with set values. 
  :param apple:   int
  :param banana:  int
  :param orange:  int
  :param grape:   int (optional value = 2)
  :param mango:   int (optional value = 3)
  :print: prints an object of integers.
  """
  print (apple, banana, orange, grape, mango)

fruitBasket(3, 6, 9, 12, 15)

# 4.) Write a program with 2 functions.
  # 1st function should take an integer as a parameter and return the result of the integer divided by 2.
  # 2nd function should take an integer as a parameter and return the result of the integer multiplied by 4.
  # Call the first function, save the result as a variable, and pass it as a parameter to the second function.

def first(x):
  """
  Returns integer divided by 2.
  :param x: int
  :return: int sum of x divided by 2.
  """
  return x / 2

def second(y):
  """
  Returns integer multiplied by 4.
  :param y: int
  :return: int sum of y multiplied by 4.
  """
  return y * 4

firstNum = first(20)
print (firstNum)

secondNum = second(firstNum)
print(secondNum)

# 5.) Write a function that converts a string to a "float" and returns the result. Use exception handling to catch the exception that could occur.

def convertFloat():
  """
  Returns a float being converted from string, prevents ValueError.
  :input a: string
  :float a: float
  :print: new float
  If ValueError is presented, print "Not a number".
  """
  try:
    a = input("Type a number: ")
    a = float(a)
    print (a)
  except (ValueError) :
    print ("Not a number.")
    
convertFloat()

# 6.) Add a docstring to all of the functions you wrote in challenges 1-5