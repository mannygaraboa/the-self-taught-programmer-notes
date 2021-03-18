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

#Function without a return statement --> returns "None"
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

age = input("Enter yout age:")
int_age = int(age)
if int_age < 21:
    print("You are young!")
else:
    print("Wow, you are old!")


# ===========================================================================
# - Reusing Functions - Pg. 54
# ===========================================================================

def even_odd(x):
  if x % 2 == 0:
    print ("even")
  else:
    print ("odd")

even_odd(2)
even_odd(3)