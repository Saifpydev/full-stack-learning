text = "language12345"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())


# Check Start End

email = "saif@gmal.com"
print(email.startswith("saif"))
print(email.endswith(".com"))


#   join String

words =  ["Python", "is", "easy"]
sentence = " ".join(words)
print(sentence)