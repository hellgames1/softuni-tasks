""""
Task 4 - Search
"""
count = int(input())
search = input()
stringswith = []
strings = []
for i in range(count):
    str = input()
    strings.append(str)
    if search in str:
        stringswith.append(str)
print(strings)
print(stringswith)