""""
Task 5 - Emoticon Finder
"""
import re
pattern = r":."
text = input()
matches = re.findall(pattern,text)
for match in matches:
    print(match)