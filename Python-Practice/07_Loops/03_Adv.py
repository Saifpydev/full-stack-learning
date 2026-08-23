# Take a number from the user and calculate its factorial using  a loop

num = int(input("Enter a number: "))

factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
    print("factorial:  ", factorial)


# Print the Fibonacci series up to n terms using a loop

# Note fibonacci series main har next number pichhle  2 numbers ka sum hota hai
n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a)
    a, b = b, a + b



# Take a number and reverse its digits using a while loop

num = int(input("Enter num: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
    print("Reversed number:", reverse)


# Take a number from the user and check whether it is a palindrome number

num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
    if original == reverse:
        print("Palindrome number")
    else:
        print("Not a palindrome nunber")

# Palindrome : EK aise number jo left s right ya right se left padne pr same rhe eg 1 -> 2 <-2 <- 1..
# 1221 same

