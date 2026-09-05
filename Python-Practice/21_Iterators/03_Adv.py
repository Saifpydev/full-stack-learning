#  Create a custom iterator that generates numbers from a given start to end

class NumberIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.end:
            number = self.current
            self.current += 1
            return number
        raise StopIteration
    
    
numbers = NumberIterator(5, 10)

for number in numbers:
    print(number) 
       

# Create a custom iterator that generates the first 10 natural numbers

class  NaturalNumbers:
    def __init__(self, n):
        self.current = 1
        self.n = n
        
    def __iter__(self):
        return self
    
    def  __next__(self):
        if self.current <= self.n:
            number = self.current
            self.current += 1
            return number
        raise StopIteration
    
    
numbers = NaturalNumbers(10) 

for number in numbers:
    print(number)   
    
        
    



# Create a custom iterator Countdown that prints


class Countdown:
    def __init__(self, start):
        self.current = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > 0:
            number = self.current
            self.current -= 1
            return number
        raise StopIteration
    
count  = Countdown(10)

for number in count:
    print(number)    
    
            

        