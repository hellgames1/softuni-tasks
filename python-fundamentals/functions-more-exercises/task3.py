""""
Task 3 - longer line
"""

from math import floor
x1, y1, x2, y2, x3, y3, x4, y4 = float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input())
dist_from_center = lambda x,y: abs(x)+abs(y)
line_length = lambda x1,y1,x2,y2: abs(x2-x1)+abs(y2-y1)
print_properly = lambda x1,y1,x2,y2: f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})" if dist_from_center(x1,y1) <= dist_from_center(x2,y2) else f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"
find_longer = lambda x1,y1,x2,y2,x3,y3,x4,y4: print_properly(x1,y1,x2,y2) if line_length(x1,y1,x2,y2) >= line_length(x3, y3, x4, y4) else print_properly(x3,y3,x4,y4)
print(find_longer(x1,y1,x2,y2,x3,y3,x4,y4))