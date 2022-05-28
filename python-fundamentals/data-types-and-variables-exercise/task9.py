""""
Task 9 - Snowballs
"""
from sys import maxsize
count = int(input())
maxvalue = -maxsize
output = ""
for i in range(count):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > maxvalue:
        maxvalue = value
        output = f"{weight} : {time} = {value:.0f} ({quality})"
print(output)