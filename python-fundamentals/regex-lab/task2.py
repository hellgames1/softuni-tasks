""""
Task 2 - Match Phone Number
"""
import re
names = input()
regex = r"\+359 2 [0-9]{3} [0-9]{4}\b|\+359-2-[0-9]{3}-[0-9]{4}\b"
matches = re.findall(regex,names)
print(", ".join(matches))