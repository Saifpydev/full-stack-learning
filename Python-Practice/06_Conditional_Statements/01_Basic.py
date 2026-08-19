# Simple if 

age = 20
if age >= 18:
    print("You are eligible")


# If False

age = 15
if age >= 18:
    print("You are eligible")

    # Note yaha prnt nhi hoga q ki condition false hai


# .if - else
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")


# Check Even /odd

number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Positive    / Negative

number = -5
if number >= 0:
    print("Positive")
else:
    print("Negative")


# IF  - elif - elif  

marks = 75
if marks >= 90:
    print("A Grade")
elif marks >= 60:
    print("B Grade")
else:
    print("C Grade")

# Multiple elif            

marks = 85
if marks >= 90:
    print("A")
elif  marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")  
else: 
    print("Fail")      


# Compare Two Numbers

a = 20
b = 10
if a > b:
    print("a is greater")
else: 
    print("b is greater")    

# Check Password    

password = "python123"
if password == "python123":
    print("Login Successful")
else:
    print("Wrong Password")













