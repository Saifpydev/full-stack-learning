# Given text = "My phone number is 9858965620" regex se 10-digit phone number extract karo.

import re

text = "My phone number is 9878986652"

result = re.search(r"\d{10}",text)

print(result.group())

# Given text = "Contact us at test@gmail.com or hello@yahoo.com regex ka use karke saare email address extract karo",..

import re

text = "Contact us at test@gmail.com or hello@yahoo.com"

emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)

print(emails)



# Given text = "Python 100, java 200, React 300" Regex se saare numbers extract karo
# ['100', "200" "3000"]



# Check karo ki user ka password valid hai ya nhi
# Requirements : Minimum 8 characters
# At least 1 uppercase letter
# At least 1 lowercase letter
# At least 1 digit

import re

password = "Saif1234"

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

if re.fullmatch(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")