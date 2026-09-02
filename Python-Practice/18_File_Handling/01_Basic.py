# file = open("data.txt", "r")
# content = file.read()
# print(content)
# file.close()  THIS IS A BASIC METHED

# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)

 # This is professional method
 # company m yahi mehtod used hota hai
 #  

# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("data.txt", "r") as file:
#     line = file.readline()
#     print(line)

# with open("data.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)


# with open("data.txt", "w") as file:
#     file.write("Python File Handling")

# with open("data.txt", "w") as file:
#     file.write("Python\n")
#     file.write("Django\n")
#     file.write("Full Stack Development\n")


# with open("data.txt", "a")as file:
#     file.write("React\n")

# with open("data.txt", "a") as file:
#     file.write("JavaScript\n")
#     file.write("BootStrap\n")
#     file.write("TailwindCSS\n")

# writtelines()

# lines = [
#     "HTML\n",
#     "CSS\n",
#     "JavaScript\n"
# ]
# with open("data.txt", "a") as file:
#     file.writelines(lines)

# tell()
# with open("data.txt", "r") as file:
#     print(file.tell())
#     file.read(10)
#     print(file.tell())

# seek()
with open("data.txt", "r") as file:
    print(file.read(10))
    file.seek(0)
    print(file.read(10))