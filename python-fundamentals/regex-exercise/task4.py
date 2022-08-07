""""
Task 4 - Extract Emails
"""
import re
pattern = r"(?<=\s)([a-z0-9]+[a-z0-9\.\-\_]*@[a-z0-9][a-z0-9\-]+[a-z0-9](\.[a-z]+)+)\b"
text=input()
matches = re.findall(pattern," "+text)
for match in matches:
    print(match[0])