""""
Task 10 - Company Users
"""
dicti={}
while True:
    command = input()
    if command=="End":
        break
    com = command.split(" -> ")
    if com[0] in dicti.keys():
        if com[1] not in dicti[com[0]]:
            dicti[com[0]].append(com[1])
    else:
        dicti[com[0]]=[com[1]]
for key in dicti.keys():
    print(key)
    for idd in dicti[key]:
        print(f"-- {idd}")