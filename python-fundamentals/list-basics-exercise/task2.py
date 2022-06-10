""""
Task 2 - Multiples List
"""
factor = int(input())
count = int(input())
current = factor
print("["+str(current),end="")
for i in range(count-1):
    current+=factor
    print(", "+str(current),end="")
print("]")