# Create a function that takes a number and return whether it is even or odd.,
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(258))
print(check_even_odd(2589))

# Create a function that takes a number and returns factorial

def factorial(num):
    result  = 1
    for i in range(1, num + 1):
        result = result * i
    return result
print(factorial(5))
print(factorial(4))


# create a function that takes a list of numbers and returns the largest numbers
def largest_list_of_num(a, b, c, d, e):
    return max(a, b, c, d, e)
print(largest_list_of_num(250, 356, 4895, 25610, 12597))
