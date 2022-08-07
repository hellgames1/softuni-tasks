""""
Task 5 - Digits, Letters and Other
"""
digits=""
letters=""
others=""
for char in input():
    if char.isdigit():
        digits+=char
    elif char.isalpha():
        letters+=char
    else:
        others+=char
print(digits)
print(letters)
print(others)