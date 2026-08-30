# Nonlocal Counter
# create a function counter() that contains a variable count  = 0 and returns an inner function..Every time the returned function is called count should increase by 1.

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


c = counter()

print(c())
print(c())
print(c())


# Closure + Scope
# create an outer() function that accepts a value and returns an inner function. The inner function should remeber the outer value and add it to a number passed later.

def outer(value):
    def inner(number):
        return value + number

    return inner

add_10 = outer(10)

print(add_10(5))
print(add_10(20))
