# Class & Object

# Create a student class with name and age. Create 2 object and print their details
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Saif", 21)
student2 = Student("Ahnad", 22)   
print("Student 1:")
print("Name:", student1.name)
print("Age:", student1.age)    

print("\nStudent 2:")
print("Name:", student2.name)
print("Age:", student2.age)        




# Constructor
# Create a Car class using _init_() with: brnad model price create an object and print all details,

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
car1 = Car("Toyota", "Fortuner", 700000000)        

print("Barnd:", car1.brand)
print("Model:", car1.model)
print("Price:", car1.price)
        


# 03 Instance Method Create a Rectangle class with length and width. Create a method area() that return the area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle1 = Rectangle(10, 5)
print("Area:", rectangle1.area())
        