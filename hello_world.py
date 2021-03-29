import math

def convertFloat():
    try:
        a = input("Type a number: ")
        a = float(a)
        print (a)
    except (ValueError) :
        print ("Not a number.")
    
convertFloat()
