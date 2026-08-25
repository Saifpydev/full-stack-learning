# Create a list of 3 fruits and insert "Orange" at index 1.

fruits = ["Mango", "apple", "lichi"]
fruits[1] = "Orange"
print(fruits)


# extend()
# Create num = [10, 20, 30]
# Add [40, 50, 60]


num = [10, 20, 30]
num.extend([40, 50, 60])
print(num)


# Remove() and pop() num = [10, 20, 30, 40, 50]
# Remove 30 using remove() remove the last item using pop()
# print the final list.

num = [10, 20, 30, 40, 50]
num.remove(30)
num.pop()
print(num)

# .sort () and reverse() 
# sort the list in ascending order, then reverse it.

num = [50, 10, 40, 20, 30]
num.sort()
print(num)
num.reverse()
print(num)

# Create index() and count() 

# num = [10, 20, 10, 30, 10, 40]
# find index of 30 Number of times 10 occurs 

num = [10, 20, 10, 30, 10, 40]
print(num.index(30))
print(num.count(10))