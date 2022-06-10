""""
Task 4 - Balanced Brackets
"""
opened = False
balanced = True
count = int(input())
for i in range(count):
    inp = input()
    if not opened and inp == "(":
        opened = True
        balanced = False
    elif not opened and inp == ")":
        balanced = False
        break
    elif opened and inp == ")":
        opened = False
        balanced = True
    elif opened and inp == "(":
        balanced = False
        break
if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")