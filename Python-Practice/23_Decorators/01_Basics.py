# .Create a decorator greet_decorator that prints
# Welcome Hello Saif

def greet_decorator(func):
    def wrapper():
        print("Welcome")
        func()
        print("Hello Saif")
        
    return wrapper    

@greet_decorator
def greet():
    print("Good Morning")

greet()


# create a decorator that prints Function started function finished around an add (a, b) function Expected: Function started 30 function finished

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function finished")
        return result
    
    return wrapper


@log_decorator
def add(a, b):
    return a + b


print(add(10, 20))


# Create a decorator that can handle any arguments using *args and **kwargs. Apply it to: def introduce(name, age): print(name, age)


def info_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function finished")
        return result
    
    return wrapper


@info_decorator
def introduce(name, age):
    print(f"My name is {name}, and I am {age} years old.")
    
introduce("Saif", 22)    