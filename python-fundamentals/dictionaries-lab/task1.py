""""
Task 1 - Bakery
"""
bakery = [a if index % 2 == 0 else int(a) for index,a in enumerate(input().split())]
print({bakery[i]:bakery[i+1] for i in range(0, len(bakery), 2)})