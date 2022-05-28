""""
Task 4 - Sum of Chars
"""
count = int(input())
sum = 0
for i in range(count):
    sum += ord(input())
print(f"The sum equals: {sum}")