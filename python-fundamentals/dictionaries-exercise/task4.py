""""
Task 4 - Phonebook
"""
dicti={}
while True:
    command = input()
    if command.isdigit():
        break
    com = command.split("-")
    dicti[com[0]] = com[1]

for i in range(int(command)):
    name = input()
    if name in dicti.keys():
        print(f"{name} -> {dicti[name]}")
    else:
        print(f"Contact {name} does not exist.")