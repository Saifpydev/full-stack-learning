# Global Varible Access
# Create a global variable language = "Python" and access it inside a function without using global

language = "Python"

def show_language():
    print(language)

show_language()



# Global  variable update
# Create a global variable score = 0. Create a function that  increases it by 10 using the glboal keyword.

score = 0
def increase_score():
    global score
    score += 10
increase_score()
print(score)    


# Enclosing Scope
# Create an outer() function with x = 100 and an inner() function with x = 50. Print x from both functions and obsere the difference

def outer():
    x = 100

    def inner():
        x = 50
        print("Inner:", x)

    print("Outer:", x)
    inner()
outer()        


# nonlocal
# Create an outer() function with count = 0. Inside innner(), nonlocal to increase count by 1 Call inner() three times and print the final value



# LEGB
# Create variables with the same name in Global, Enclosing, and local scopes. Access the variable from the inner function and identify which value python selects according to the LEGB rule

