""""
Task 7* - Easter Gifts
"""
gifts = input().split(" ")
while True:
    command = input()
    if command == "No Money":
        break
    else:
        com = command.split(" ")
        if com[0]=="OutOfStock":
            for index,item in enumerate(gifts):
                if item==com[1]:
                    gifts[index]="None"
        if com[0]=="Required":
            if 0 <= int(com[2]) < len(gifts):
                gifts[int(com[2])] = com[1]
        if com[0]=="JustInCase":
            gifts.pop()
            gifts.append(com[1])
printed = ""
for item in gifts:
    if item != "None":
        printed += item + " "
print(printed[:-1])