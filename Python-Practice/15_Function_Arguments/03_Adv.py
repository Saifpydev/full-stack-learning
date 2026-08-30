
# Keyword-only Arguments
# creat a function
def employee(name, *, role, salary):
    print("Name:", name)
    print("Role:", role)
    print("Salary:", salary)

employee("Saif", role="Developer", salary= 5000000)    

# Call it correctly using a positional argument for name and keyword argumets for role and salary



# positional-only- Arguments

# create a function

def student(name, age, /, city):
        print("Name:", name)
        print("Age:", age)
        print("City:", city)
student("Saif", 22, city ="Delhi")        


    # Call it using positional arguments for name and age.
