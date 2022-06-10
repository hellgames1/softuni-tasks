""""
Task 5 - Numbers Filter
"""
even = []
odd = []
positive = []
negative = []
for i in range(int(input())):
    num = int(input())
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
print(globals()[input()])