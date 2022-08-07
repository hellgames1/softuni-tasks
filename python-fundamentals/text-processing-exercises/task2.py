""""
Task 2 - Character Multiplier
"""
strs = input().split()
if len(strs[0]) >= len(strs[1]):
    longer = 0
else:
    longer = 1
result = 0
for i in range(len(strs[longer])):
    try:
        result += ord(strs[0][i]) * ord(strs[1][i])
    except IndexError:
        result += ord(strs[longer][i])
print(result)