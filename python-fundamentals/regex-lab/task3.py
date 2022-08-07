""""
Task 3 - Match Dates
"""
import re
names = input()
regex = r"\b(\d{2})(\.|\-|/)([A-Z][a-z]{2})\2(\d{4})\b"
matches = re.findall(regex,names)
for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")