""""
Task 10 - bread factory
"""
inp = input().split("|")
events=[]
energy=100
coins=100
closed=False
for event in inp:
    temp = event.split("-")
    events.append([temp[0],int(temp[1])])

for event in events:
    if event[0]=="rest":
        if energy+event[1]>100:
            print(f"You gained {100-energy} energy.")
        else:
            print(f"You gained {event[1]} energy.")
        energy+=event[1]
        if energy>100:
            energy=100
        print(f"Current energy: {energy}.")
    elif event[0]=="order":
        if energy>=30:
            energy-=30
            coins+=event[1]
            print(f"You earned {event[1]} coins.")
        else:
            energy+=50
            print("You had to rest!")
    else:
        if coins>=event[1]:
            coins-=event[1]
            print(f"You bought {event[0]}.")
        else:
            print(f"Closed! Cannot afford {event[0]}.")
            closed=True
            break
if not closed:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")