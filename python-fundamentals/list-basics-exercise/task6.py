""""
Task 6 - Survival of the Biggest
"""
from sys import maxsize
ints=[]
for num in input().split(" "):
    ints.append(int(num))
count = int(input())
for i in range(count):
    siz = maxsize
    for j in ints:
        if j<siz:
            siz = j
    ints.remove(siz)
print(str(ints).replace("[","").replace("]",""))