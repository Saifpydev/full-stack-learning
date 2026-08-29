# create a list containing the cubes of numbers from 1 to 10 using list Comprehension

cubes = [x**3 for x in range (1,11)]
print(cubes)

# Given Create a new list containing only numbers greater than 15

numbers = [1, 2, 3, 4, 5, 6, 7,]
result = [x for x in numbers if x > 15]
print(result)



# Given words create a new list containing the length of each word

words = ["Python", "Django", "react"]

lengths = [len(word) for word in words]
print(lengths)


# given numbers create a new list containing the square the squares of only even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 8]

square = [x**2 for x in numbers if x % 2 == 0]
print(square)

