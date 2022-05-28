""""
Task 10 - Gladiator Expenses
"""
count = int(input())
prices = [float(input()), float(input()), float(input()), float(input())]
cost = 0
# helmet, sword, shield, armor
for i in range(1, count + 1):
    if i % 2 == 0:
        cost += prices[0]
    if i % 3 == 0:
        cost += prices[1]
        if i % 2 == 0:
            cost += prices[2]
    if i % 12 == 0:
        cost += prices[3]
print(f"Gladiator expenses: {cost:.2f} aureus")