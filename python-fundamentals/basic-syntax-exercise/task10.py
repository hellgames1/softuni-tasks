""""
Task 10 - Mutate Strings
"""

first = input()
second = input()
length = len(first)
result = "a"
lastresult = first
for i in range(1, length+1):
    result = second[:i]+first[i:]
    if result != lastresult:
        print(result)
        lastresult = result