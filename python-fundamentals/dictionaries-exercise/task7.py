""""
Task 7 - SoftUni Parking
"""
dicti={}
count = int(input())
for i in range(count):
    com = input().split()
    if com[0]=="register":
        if com[1] not in dicti.keys():
            dicti[com[1]] = com[2]
            print(f"{com[1]} registered {com[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {dicti[com[1]]}")
    elif com[0]=="unregister":
        if dicti.pop(com[1], None) is not None:
            print(f"{com[1]} unregistered successfully")
        else:
            print(f"ERROR: user {com[1]} not found")
for let,num in dicti.items():
    print(f"{let} => {num}")