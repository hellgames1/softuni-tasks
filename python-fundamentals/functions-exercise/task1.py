""""
Task 1 - Smallest of Three Numbers
"""
from sys import maxsize
def smallest_of_three(num1,num2,num3):
    smallest=maxsize
    for i in [num1,num2,num3]:
        if i<smallest:
            smallest=i
    return smallest
print(smallest_of_three(int(input()),int(input()),int(input())))