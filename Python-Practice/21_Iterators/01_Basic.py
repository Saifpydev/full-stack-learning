numbers = [10, 20, 30 ,80, 40, 90, 50]
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))



# Create a tuple: 
# convert it into an iterator and use next() to print each name.

names = ("saif", "Rahul", "Aman")
it = iter(names)
print(next(it))
print(next(it))
print(next(it))


# Create a string Convert it into an iterator and print its characters one by one using next()

word  = "Pyhton"

it = iter(word)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# create a list Use an itertor and next() to print the values Then try one extra next() and observe StopitERATION

numbers = [10, 20, 30]
it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))

# Create a custom iterator that iterates through a list in reverse order

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1
        
    def __int__(self):
        return self
    
    def __next__(self):
        
        if self.index < 0:
            raise StopIteration
        
        value = self.data[self.index]
        self.index -= 1
        
        return value
    
numbers = [10, 20, 30, 40, 60, 50]
    
it = ReverseIterator(numbers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
