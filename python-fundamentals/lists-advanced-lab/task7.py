""""
Task 7 - The Office
"""
from math import ceil
emps = [int(a) for a in input().split(" ")]
improvement = int(input())
average = 0
amount = len(emps)
for i in range(amount):
    emps[i] *= improvement
    average += emps[i]
average /= amount
happy_amount = len([a for a in emps if a >= average])
if happy_amount >= ceil(amount/2):
    print(f"Score: {happy_amount}/{amount}. Employees are happy!")
else:
    print(f"Score: {happy_amount}/{amount}. Employees are not happy!")