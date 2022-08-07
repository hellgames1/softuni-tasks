""""
Task 6 - Orders
"""
dicti={}
while True:
    command = input()
    if command == "buy":
        break
    com = command.split()
    if com[0] in dicti.keys():
        dicti[com[0]][0]=float(com[1])
        dicti[com[0]][1]+=int(com[2])
    else:
        dicti[com[0]]=[float(com[1]),int(com[2])]
for let,num in dicti.items():
    print(f"{let} -> {(num[0] * num[1]):.2f}")