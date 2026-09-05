# Create a custom iterator that returns characters of a string i reverse order.

class ReverseString:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= 0:
            char = self.text[self.index]
            self.index -= 1
            return char
        raise StopIteration
    
word = ReverseString("Python")  
for char in word:
    print(char)  
       
        








# Create a custom iterator for  numbers 1-100 that returns only even numbers


