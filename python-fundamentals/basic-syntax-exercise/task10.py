""""
You will be given two strings.
Transform the first string into the second one, letter by letter, starting from the first one.
After each interaction, print the resulting string only if it is unique.
Note: the strings will have the same length
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