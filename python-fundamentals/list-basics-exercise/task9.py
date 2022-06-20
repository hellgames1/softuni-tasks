""""
Task 9 - Hello, France
"""
inp = input().split("|")
items=[]
budget=float(input())
floatingbudget = budget
inventory=""
profit=0
for item in inp:
    temp = item.split("->")
    items.append([temp[0],float(temp[1])])
for item in items:
    if (item[0]=="Clothes" and item[1]<=50) or (item[0]=="Shoes" and item[1]<=35) or (item[0]=="Accessories" and item[1]<=20.5):
        if item[1]<=floatingbudget:
            floatingbudget-=item[1]
            inventory+=f"{(item[1]*1.4):.2f} "
            profit+=item[1]*0.4
print(inventory[:-1])
print(f"Profit: {profit:.2f}")
if budget+profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")