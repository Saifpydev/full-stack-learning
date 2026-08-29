# Given Using dictionary comprehension create  a new dictionary containing only sudents who scored 80 or above..

students = {
    "Saif": 85,
    "Ahmad": 82,
    "Raja": 50,
    "Dabloo": 52,
    "Raji": 81,
}
result = {name: marks for name, marks in students.items() if marks >= 80}
print(result)
