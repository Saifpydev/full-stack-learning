# Check whether a number is positive negative or 0.

num = 100
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Num is zero")


# Create a login system with: Username Password if both are correct > Login successful otherwise invalid username or password
     
username = "admin"  
password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Invalid username or password")

# New question same method used

username = "Saif farid"
password = "7004742819"

username = input("Enter username: ")
password = input("Enter password: ")
if username == "Saif farid" and  password == "12345":
    print("Login successful")
else:
    print("Invalid username or password")