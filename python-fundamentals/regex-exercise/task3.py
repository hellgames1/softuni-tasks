""""
Task 3 - Find Occurences of Word in Sentence
"""
import re
text=input()
pattern = input()
print(len(re.findall("\\b"+pattern+"\\b",text,re.IGNORECASE)))
