# Print all numbers from 1 to 50 that are divisible by 3.
for i in range(1, 51):
    if i % 3 == 0:
        print(i)




# Take a number from the user and calculate the sum of its digits

num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits = sum_digits + digit
    num = num // 10
    print("Sum of digits: ", sum_digits)




# Ṭake a number from the user and check whether it is a prime number..

num = int(input("Enter a number: "))
if num <= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

        if is_prime:
            print("Prime number")
        else:
            print("Not a prime number")











