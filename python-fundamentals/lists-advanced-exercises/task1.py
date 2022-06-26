""""
Task 1 - Which Are In
"""
substrings = []
for stri in input().split(", "):
    substrings.append([stri,False])
strings = input().split(", ")
for substr in substrings:
    for stri in strings:
        if substr[0] in stri:
            substr[1] = True
            break
result = [a[0] for a in substrings if a[1]]
print(result)