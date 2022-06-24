""""
Task 4 - Palindrome Strings
"""
words = input().split(" ")
lookup = input()
found=[]
occurences=0
for word in words:
    if word == word[::-1]:
        found.append(word)
    if word==lookup:
        occurences+=1
print(found)
print(f"Found palindrome {occurences} times")