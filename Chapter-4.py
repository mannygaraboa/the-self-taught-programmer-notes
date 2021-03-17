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

