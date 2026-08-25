# Create a list of 10 numbers and find the largest, smallest, and total sum.

numbers = [10, 20, 40, 50, 400, 78, 780, 999, 478]
total = sum(numbers)
print(numbers)
print(max(numbers))
print(min(numbers))
print(total)


# Create a list of numbers and seperate the even and odd numbers into two different list.

Num = [10, 256, 56, 456, 123, 782, 452]
even = []
odd = []
for i in Num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)        