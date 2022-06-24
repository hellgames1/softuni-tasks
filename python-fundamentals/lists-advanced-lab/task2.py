""""
Task 2 - Trains
"""
count = int(input())
wagons = [0]*count
while True:
    command = input()
    if command == "End":
        break
    com = command.split(" ")
    if com[0]=="add":
        wagons[len(wagons)-1]+=int(com[1])
    elif com[0]=="insert":
        wagons[int(com[1])]+=int(com[2])
    elif com[0]=="leave":
        wagons[int(com[1])]-=int(com[2])
print(wagons)