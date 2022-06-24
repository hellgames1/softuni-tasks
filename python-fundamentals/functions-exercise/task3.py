""""
Task 3 - Characters in Range
"""
char1 = ord(input())
char2 = ord(input())
result = lambda x,y: [chr(i) for i in range(x+1,y)]
print(*result(char1,char2))