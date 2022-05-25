""""
Task 2 - Find the Capitals
"""
word = input()
list_capitals = []
for index, letter in enumerate(word):
    if letter.isupper():
        list_capitals.append(index)
print(list_capitals)