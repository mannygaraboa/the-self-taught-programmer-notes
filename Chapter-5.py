# ===========================================================================
# Chapter 5: Containers
# ===========================================================================

# ===========================================================================
# - Methods - Pg. 67
# ===========================================================================

# Methods: functions closely associated with a given type of data.
# Methods execute code and can return a result just like a function.
# Unlike a function, you call a method on an object.

"Hello".upper()                       # >> "HELLO"
"Hello".replace("o", "@")             # >> "Hell@"

# ===========================================================================
# - Lists - Pg. 67
# ===========================================================================

# List: A container that stores objects in a specific order.

fruit = list()  # >> []
fruit = []      # >> []

fruit = ["Apple", "Orange", "Pear"]
fruit.append("Banana")                # >> ['Apple', 'Orange', 'Pear', 'Banana']
fruit.append("Peach")                 # >> ['Apple', 'Orange', 'Pear', 'Banana', 'Peach']
print (fruit)



# Lists can store any data type:

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")                # >> [True, 100, 1.1, 'Hello']
print (random[2])                     # >> 1.1
# print (random[4])                   # >> IndexError: list index out of range



# Strings, lists and tuples are "iterable".
# An object is iterable when you can access each item using a loop.
# Iterables: Objects that are iterable. 
# Each item in an iterabe has an "index" - a number representing the item's position in the iterable.

print (fruit[0])                      # >> "Apple"
print (fruit[1])                      # >> "Orange"
print (fruit[2])                      # >> "Pear"



# Lists are "mutable".
# When a container is mutable, you can add or remove objects from the container.
# You can change an item in a list by assigning its index to a new object:

colors = ["blue", "green", "yellow"]
colors[2] = "red"                     # >> ["blue", "green", "red"]
print (colors)

# 'pop' method: remove the last item from a list.

item1 = colors.pop()
print (colors)                        # >> ['blue', 'green']
print (item1)                         # >> 'red'

# You cannot use 'pop' on an empty list >> IndexError: pop from empty list

# Combine 2 lists with the addition operator:

colors1 = ["blue", "green", "yellow"]
colors2 = ["orange", "pink", "black"]
print (colors1 + colors2)             # >> ['blue', 'green', 'yellow', 'orange', 'pink', 'black']

# in: Check if an item is in a list

"green" in colors1                    # >> True
"green" in colors2                    # >> False

# not: Check if an item is not in a list

"black" not in colors1                # >> True
"black" not in colors2                # >> False

# len: Get the size of a list (the number of items in it)

len(colors1)                          # >> 3

colors3 = ["purple",
           "orange", 
           "green"]
guess = input("Guess a color: ")
if guess in colors3:
  print ("You guessed correctly!")
else:
  print ("Wrong! Try again.")


# ===========================================================================
# - Tuples - Pg. 73
# ===========================================================================

# Tuple: Container that stores objects in a specific order. 
# Tuples are immutable --> contents cannot change.

my_tuple1 = tuple()
my_tuple2 = ()

rndm = ("M. Jackson", 1958, True)
print (rndm)

# Even if a tuple only has 1 item, you need to put a comma after it.

("self_taught",)                        # >> this is a tuple
(9) + 1                                 # >> this is not a tuple

# Cannot add new items to a tuple or change it once created --> Python raises exception

dys = ("1984",
       "Brave New World",
       "Fahrenheit 451")
# dys[1] = "Handmaid's Tale"            # >> TypeError: 'tuple' object does not support item assignment
print (dys[2])                          # >> "Fahrenheit 451"
print ("1984" in dys)                   # >> True
print ("Handmaid's Tale" not in dys)    # >> True



# ===========================================================================
# - Dictionaries - Pg. 76
# ===========================================================================

# Dictionaries: Another built-in container for storing objects.
# Used to link one object, called a 'key', to another object -- called the 'value'.
# Mapping: Linking one object to another --> resulting in a 'key-value pair'.
# Add 'key-value pairs' to a dictionary.

# Can look up a key in the dictionary to get its value.
# Cannot use a value to look up a key.

# Dictionaries are mutable --> can add new key-value pairs.
# Do not store objects in a specific order.

# For example: could store information about someone in a dictionary.

my_dict1 = dict()
my_dict2 = {}
print (my_dict1)                         # >> {}

fruits1 = {"Apple" : "Red",
           "Banana" : "Yellow"}
print (fruits1)                          # >> {'Apple': 'Red', 'Banana': 'Yellow'}


# Once dictionary is created, add key-value pair --> [dictionary_name][[key]] = [value]
# Look up a value using a key --> [dictionary_name][key]

facts = dict()

# add a value
facts["code"] = "fun"
# look up a key
print (facts["code"])                    # >> "fun"

facts["Bill"] = "Gates"
print (facts["Bill"])                    # >> "Gates"

facts["founded"] = 1776
print (facts["founded"])                 # >> 1776

# Unlike a dictionary value, a dictionary key must be immutable.
# A string or a tuple can be a dictionary key, but not a list or a dictionary.

# Use 'in' to check if a key is in a dictionary.
# Cannot use 'in' to check if a value is in a dictionary.
# keyword 'not' to 'in' to check if a key is not in a dictionary.

bill = {"Bill Gates" : "charitable"}
print ("Bill Gates" in bill)             # >> True
print ("Bill Doors" not in bill)         # >> True

# If you try to access a key that isn't in a dictionary, Python will raise an exception.

# You can delete a key-value pair from a dictionary with the keyword 'del'.

books = {"Dracula" : "Stoker", 
         "1984" : "Orwell",
         "The Trial" : "Kafka"}
del books["The Trial"]                   
print (books)                            # >> {'Dracula': 'Stoker', '1984': 'Orwell'}

rhymes = {
          1: "fun",
          2: "blue",
          3: "me",
          4: "floor",
          5: "live"
         }

n = input("Type a number: ")
if n in rhymes:
    rhyme = rhymes[n]
    print (rhyme)
else:
    print ("Not found.")

