""""
Task 1 - Capture the Numbers
"""
import re
pattern = r"\d+"
text=""
while True:
    try:
        text += input()
    except EOFError:
        break
print(" ".join(re.findall(pattern,text)))
