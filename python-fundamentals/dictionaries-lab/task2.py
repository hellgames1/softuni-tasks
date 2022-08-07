""""
Task 2 - Stock
"""
bakery = input().split()
print(*["We have "+{bakery[i]:bakery[i+1] for i in range(0, len(bakery), 2)}[item]+" of "+item+" left" if item in {bakery[i]:bakery[i+1] for i in range(0, len(bakery), 2)} else f"Sorry, we don't have {item}" for item in input().split()],sep="\n")
# LOL