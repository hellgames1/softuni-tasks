""""
Task 12 - Christmas Spirit
"""

count = int(input())
days_left = int(input())
cost = 0
spirit = 0
for i in range(1,days_left+1):
    if i % 11 == 0:
        count += 2
    if i % 2 == 0:
        cost += 2 * count
        spirit += 5
    if i % 3 == 0:
        cost += 8 * count
        spirit += 13
        if i % 5 == 0:
            spirit += 30
    if i % 5 == 0:
        cost += 15 * count
        spirit += 17
    if i % 10 == 0:
        spirit -= 20
        cost += 23
if days_left % 10 == 0:
    spirit -= 30
print(f"Total cost: {cost}\nTotal spirit: {spirit}")