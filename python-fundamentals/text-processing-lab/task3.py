""""
Task 3 - Substring
"""
subs = input()
whole = input()
while subs in whole:
    whole = whole.replace(subs,"")
print(whole)