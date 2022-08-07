""""
Task 8 - Courses
"""
dicti={}
while True:
    command=input()
    if command=="end":
        break
    com = command.split(" : ")
    if com[0] not in dicti.keys():
        dicti[com[0]]=[com[1]]
    else:
        dicti[com[0]].append(com[1])
for key in dicti.keys():
    ln = len(dicti[key])
    print(f"{key}: {ln}")
    for i in range(ln):
        print(f"-- {dicti[key][i]}")