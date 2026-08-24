# Change Case 

text  = "Python programming"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())

# Remove Extra Space

text = "    I   LOVE    Java  "
new_text = text.replace("Java","Python")
print(new_text)

# Find & Count
text = "Python is easy and Python is powerful"
print(text.find("Python"))
print(text.count("Python"))