""""
Task 5 - Office Chairs
"""
from sys import maxsize
rooms_amount = int(input())
chairs_free = 0
for room in range(1, rooms_amount + 1):
    command = input()
    com = command.split()
    chairs_amount = com[0].count("X")
    chairs_needed = int(com[1]) - chairs_amount
    if chairs_needed > 0:
        print(f"{chairs_needed} more chairs needed in room {room}")
        chairs_free = -maxsize
    else:
        chairs_free -= chairs_needed
if chairs_free >= 0:
    print(f"Game On, {chairs_free} free chairs left")