# ===========================================================================
# Chapter 5: Containers
# ===========================================================================

# ===========================================================================
# - Methods - Pg. 67
# ===========================================================================

# Methods: functions closely associated with a given type of data.
# Methods execute code and can return a result just like a function.
# Unlike a function, you call a method on an object.

"Hello".upper()             # >> "HELLO"
"Hello".replace("o", "@")   # >> "Hell@"

# ===========================================================================
# - Lists - Pg. 67
# ===========================================================================

# List: A container that stores objects in a specific order.

fruit = list()  # >> []
fruit = []      # >> []

fruit = ["Apple", "Orange", "Pear"]
fruit.append("Banana")        # >> ['Apple', 'Orange', 'Pear', 'Banana']
fruit.append("Peach")         # >> ['Apple', 'Orange', 'Pear', 'Banana', 'Peach']
print (fruit)



# Lists can store any data type:

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")        # >> [True, 100, 1.1, 'Hello']
print (random[2])             # >> 1.1
# print (random[4])           # >> IndexError: list index out of range

