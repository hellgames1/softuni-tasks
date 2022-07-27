""""
Task 9 - Anonymous Threat
"""
strings = input().split()
newstrings = []
while True:
    command = input()
    if command == "3:1":
        break
    com = command.split()
    start, end = int(com[1]), int(com[2])
    if start < 0:
        start = 0
    if com[0]=="merge":
        if end >= len(strings):
            end = len(strings)-1
        temp = ""
        for i in range(start, end+1):
            temp += strings[i]
        for i in range(start, end+1):
            strings.pop(start)
        strings.insert(start,temp)
    elif com[0]=="divide":
        working = strings[start]
        strings.pop(start)
        single = len(working) // end
        divided = []
        while True:
            if len(divided)<end-1:
                divided.append(working[:single])
                working = working[single:]
            else:
                divided.append(working)
                break
        for i, x in enumerate(divided):
            strings.insert(start+i,x)



print(*strings,sep=" ")