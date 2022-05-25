""""
Task 11 - Easter Bread
"""
budget = float(input())
price_flour = float(input())

price_eggs = price_flour * 0.75
price_milk = price_flour * 1.25 * 0.25
price_bread = price_flour + price_eggs + price_milk

breads_count = int(budget / price_bread)
budget -= breads_count * price_bread

eggs = 3 * breads_count
for i in range(breads_count // 3):
    eggs -= (i + 1) * 3 - 2

print(f"You made {breads_count} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")