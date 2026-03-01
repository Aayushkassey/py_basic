# import re

# text= "My phone number is 123-456-7890."

# pattern = r"\d{3}-\d{3}-\d{4}"

# match = re.search(pattern, text)
# if match:
#     print("Phone number found:", match.group())

import re 

email_regex= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

email= "surump3@gmail.com"

if re.match(email_regex, email):
    print(f"Valid Email address")
else:
    print(f"Invalid email Address")