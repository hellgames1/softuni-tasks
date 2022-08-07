""""
Task 2 - Repeat Strings
"""
result=""
strs = input().split()
for st in strs:
    result+=st*len(st)
print(result)