# Ṃultiple Imports
# Import math and random moudules and:

import math
import random

# Find the square root of 81

print("Square Root:", math.sqrt(81))

# Generate a random number between 1 and 50
random.randint(1, 50)


# Module Alias
# Import datetime using an alias and print the current date.

import datetime as dt

print("Current Date:", dt.date.today())

# Custom Module
# Crete calculator.py containing
# add()
# subtract()
# multiple()
# divide()

import _Calculator

print("Add:", _Calculator.add(10, 5))
print("Subtract:", _Calculator.subtract(10, 5))
print("Multiply:", _Calculator.multiply(10, 5))
print("Divide:", _Calculator.divide(10, 5))