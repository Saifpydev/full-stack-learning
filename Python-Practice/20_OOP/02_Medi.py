# Create a Student class with a class variable school = "ABC School"
# Create 2 Object and pritn each studnets name and school

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

student1 = Student("Ram")
student2 = Student("Radha")

print("Student 1:", student1. name, student1.school)
print("Student 2:", student2. name, student2.school)
        






# Instance + Class Variable, Create a BankAccount class with: class variable bank_name instance variabales name, balance method show_details()


class BankAccount:
    bank_name = "SBI Bank"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_details(self):
        print("Bank:", self.bank_name)    
        print("Name:", self.name)
        print("Balance:", self.balance)
account1 = BankAccount("Saif", 9205622636499)
account1.show_details()



# Class Method create a Student class with a class variable school. Create a @classmethod to change the school name.

class Student:
    school = "Jain School"
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

print("Old School:", Student.school)

Student.change_school("XYZ School")
print("New School:", Student.school)
