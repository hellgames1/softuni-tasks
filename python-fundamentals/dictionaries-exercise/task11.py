""""
Task 11 - Force Book
"""
dicti={}
while True:
    command = input()
    if command=="Lumpawaroo":
        break
    if "|" in command:
        com = command.split(" | ")
        user = com[1]
        side = com[0]
        user_exists = False
        for i in dicti.keys():
            if user in dicti[i]:
                user_exists = True
                break
        if not user_exists:
            if side not in dicti.keys():
                dicti[side]=[user]
            else:
                dicti[side].append(user)
    elif "->" in command:
        com = command.split(" -> ")
        user = com[0]
        side = com[1]
        user_exists = (False, "wtf")
        for i in dicti.keys():
            if user in dicti[i]:
                user_exists = (True, i)
                break
        if user_exists[0]:
            dicti[user_exists[1]].remove(user)
        if side not in dicti.keys():
            dicti[side]=[user]
        else:
            dicti[side].append(user)
        print(f"{user} joins the {side} side!")
for key in dicti.keys():
    ln = len(dicti[key])
    if ln==0:
        continue
    print(f"Side: {key}, Members: {ln}")
    for i in range(ln):
        print(f"! {dicti[key][i]}")