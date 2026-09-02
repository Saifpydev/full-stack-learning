# write a python program that takes two numbers from the user and divides them. Handle the ZeroDivisionError using try-except.

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# try:
#     result = num1 / num2
#     print("Resilt:", result)

# except ZeroDivisionError:
#     print("Cannot divide by zero.")    



# Write a Python program that takes a number from the user and converts it into an integer using int()

# num = input("Enter a number: ")
# num = int(num)
# print = ("Integer:", num)

# Write a Python Program that takes two numbers from the user and handles both
# ValueError - invalid input
# ZeroDivisionError - division by zero 


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result: ", result)


except ValueError:
    print("Invalid input! Please enter number only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
    


