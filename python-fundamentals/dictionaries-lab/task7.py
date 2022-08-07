""""
Task 7 - Word Synonyms
"""
count = int(input())
dic = {}
for i in range(count):
    word = input()
    if word in dic:
        dic[word].append(input())
    else:
        dic[word]=[input()]
for word in dic:
    print(f"{word} - ",end="")
    print(*dic[word],sep=", ")