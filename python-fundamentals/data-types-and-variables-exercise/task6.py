""""
Task 6 - Triples of Latin Letters
"""
count = int(input())
for i in range(count):
    for j in range(count):
        for k in range(count):
            print(chr(97+i) + chr(97+j) + chr(97+k))