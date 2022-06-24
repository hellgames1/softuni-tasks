""""
Task 9 - Password Validator
"""
password = input()
password_length = lambda a: True if 6<=len(a)<=10 else print("Password must be between 6 and 10 characters")
password_chars = lambda a: True if a.isalnum() else print("Password must consist only of letters and digits")
password_digits = lambda a: True if len([x for x in a if x.isnumeric()])>=2 else print("Password must have at least 2 digits")
valid = True
if not password_length(password):
    valid = False
if not password_chars(password):
    valid = False
if not password_digits(password):
    valid = False
if valid:
    print("Password is valid")