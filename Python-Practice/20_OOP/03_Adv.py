# Combined OOP
# create person employee manager
# Use: inheritance __init__() super() method overriding instance variables 
# create a show_details() mehtod and display manager information.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)    

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee_ID:", self.employee_id)
        print("Salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print("Department:", self.department)


# Create Manager object 
manager1  = Manager("Saif", 25, "M101", 90000000, "IT")

# Display Manager Object 
manager1.show_details()
        
            
    


        
    