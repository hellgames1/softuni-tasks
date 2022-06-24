""""
Task 2 - Center Point
"""
from math import floor
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
dist_from_center = lambda x,y: abs(x)+abs(y)
if dist_from_center(x1,y1) <= dist_from_center(x2,y2):
    print(f"({floor(x1)}, {floor(y1)})")
else:
    print(f"({floor(x2)}, {floor(y2)})")