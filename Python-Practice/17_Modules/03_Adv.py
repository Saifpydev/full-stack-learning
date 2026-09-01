# Module Design
# Create math_utils.py containing functions for:
# Square Cube Factorial
# Import the module and call all functions from 

import _math_utils
print("Square:", _math_utils.square(5))
print("Cube:", _math_utils.cube(5))
print("Factorial:", _math_utils.factorial(5))



# Selective Import + Alias

# Create a module converter.py with functions
# celsius_to_fahrenheit()
# kilometers_to miles()
# Import only these functions using form ... import ... and give one imported function an alis


from converter import celsius_to_fahrenheit as c_to_f, kilometers_to_miles

print("Fahrenheit:", c_to_f(25))
print("Miles:", kilometers_to_miles(10))