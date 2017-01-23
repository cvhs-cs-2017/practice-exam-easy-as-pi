"""1. Write a function that will double any integer (n) and return the result"""

def Double(n):
    return n*2

print(Double(3))
print(Double(5))

"""2.  Write a program that will (1) ask the user for an input value, (2) take
that and double it and  (3) print the result.
Include necessary print statements and address whitespace issues."""

print('Enter any number.')
n = int(input())
print(str(n) + " multiplied by two is", str(Double(n)))
