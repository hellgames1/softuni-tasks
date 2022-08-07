""""
Task 5 - ASCII Values
"""
listt = input().split(", ")
print({listt[a]:[ord(a) for a in listt][a] for a in range(len(listt))})