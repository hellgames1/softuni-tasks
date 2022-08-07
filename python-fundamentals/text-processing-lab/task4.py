""""
Task 4 - Text Filter
"""
banned = input().split(", ")
sent = input()
for word in banned:
    sent=sent.replace(word,"*"*len(word))
print(sent)