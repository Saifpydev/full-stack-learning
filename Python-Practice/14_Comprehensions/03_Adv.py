# Given numbers create a list containing the squares of odd numbers only

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [x**2 for x in numbers if x % 2 !=0]
print(squares)


# given create a dictionary where key = word value = length of the word 
words = ["Python", "Java", "Django", "react", "sql"]

result = {word: len(word) for word in words}
print(result)
