# pop () and  clear()
# create a set of numbers, remove one item using pop().then remove all remaining items using clear()

numbers = {10, 20, 30, 40,62, 50}
print("Original:", numbers)

numbers.pop()
print("After pop:", numbers)

numbers.clear()
print("After clear:", numbers)

# Union a = {1, 2, 3}
#       B = {3, 4, 5}

# find all unique elements from both sets using union()


a = {1, 2, 3}
b = {3, 4, 5}
result = a.union(b)  # union() = dono sets ko mila do duplicate hata do

print(result)

# Intersection given : a {1, 2, 3, 4} b = {3, 4, 5, 6}
# find the elements common to both sets using intersection()

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.intersection(b)   # intersection () = common elements hai
print(result)






# Symmetric difference using a = {1, 2, 3, 4} b = {3, 4, 5, 6}
# Find the elements that are not common between the two  sets using

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result  = a.symmetric_difference(b)
print(result)