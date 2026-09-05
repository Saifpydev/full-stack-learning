# Create an iterator form use a while loop + next() to print all values Handle StopIteration
numbers = [10, 20, 30 ,50, 80, 90]

it = iter(numbers)

while True:
    
    try:
        
        print(next(it))
    except StopIteration:
        break    

# Create an iterator from a list of names and print only the first 3 values next()

names = ["Saif", "Rahul", "Aman", "Rohit", "Arman"]
it = iter(names)

print(next(it))
print(next(it))
print(next(it))



# create a custom iterator that prints even numbers from 2 to 10

class EvenNumbers:
    
    def __init__(self):
        self.number = 2
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.number > 10:
            raise StopIteration
        
        value = self.number
        self.number += 2
        return value

it = EvenNumbers() 

print(next(it))  
print(next(it)) 
print(next(it))
print(next(it))
print(next(it))





