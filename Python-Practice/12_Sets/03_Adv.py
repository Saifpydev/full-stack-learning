# Remove Duplicates 
# numbers = [10, 20, 30, 20, 40, 10, 20]
# convert the list into a set to remove duplicates then print the result

numbers = [10, 20, 30, 20, 40, 10, 20]
numbers = set(numbers)
print(numbers)





# Common Students 
Python_students = {"Saif", "Ali", "Rahul", "Aman"}
django_students = {"Rahul", "Aman", "Zaid"}

# find the students who are learning both python and django.

common_students = Python_students.intersection(django_students)
print(common_students)
