# args
# Create a function calculate_sum() that accept any number of number using args and returns their num

def calculate_sum(*args):
    total = 0

    for number in args:
        total =  total + number 

    return total

result = calculate_sum(10, 230, 30, 70)    
print("Sum:", result)

# Ṇote *args any numbers of arguments accept karta hai
#  args tuple ke form mein values store karta hai
# .for ek ek value access karta hai
# return result function ke bahar bhejta hai


# args - Maximum
# Create a function find_max() that accepts any number of using args and prints the largest numbers


def find_max(*args):
    largest = args[0]

    for number in args:
        if number > largest:
            largest = number

    return largest

print(find_max(10, 80, 55, 48, 51))    
