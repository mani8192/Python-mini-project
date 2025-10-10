# Email validation check program --

import re
# regex email_pattern
email_pattern = r"^[a-z0-9]+[._]?[a-z0-9]+[@]\w+\.\w{2,3}$"

print("=== Email Validation Check ===")

user_email = input("Enter your email address: ")

# condition--
if re.search(email_pattern, user_email):
    print(f"'{user_email}' is a valid email.")
else:
    print(f"'{user_email}' is NOT a valid email")
