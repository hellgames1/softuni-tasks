""""
Task 3 - Special Numbers
"""
count = int(input())
for i in range(1, count+1):
    current = str(i)
    currentsum = 0
    for char in current:
        currentsum += int(char)
    if currentsum == 5 or currentsum == 7 or currentsum == 11:
        print(current + " -> True")
    else:
        print(current + " -> False")