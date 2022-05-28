""""
Task 3 - Elevator
"""
people = int(input())
capacity = int(input())
courses = people // capacity
if people % capacity != 0:
    courses += 1
print(courses)