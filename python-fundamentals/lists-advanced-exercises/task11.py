""""
Task 11 - SoftUni Course Planning
"""
lessons = input().split(", ")
while True:
    command = input()
    if command == "course start":
        break
    com = command.split(":")
    if com[0]=="Add":
        if com[1] not in lessons:
            lessons.append(com[1])
    elif com[0]=="Insert":
        if com[1] not in lessons:
            lessons.insert(int(com[2]), com[1])
    elif com[0]=="Remove":
        if com[1] in lessons:
            lessons.remove(com[1])
            if com[1]+"-Exercise" in lessons:
                lessons.remove(com[1]+"-Exercise")
    elif com[0]=="Swap":
        if com[1] in lessons and com[2] in lessons:
            first_has_exercise = False
            second_has_exercise = False
            firstindex = lessons.index(com[1])
            secondindex = lessons.index(com[2])
            try:
                if lessons[firstindex+1] == com[1] + "-Exercise":
                    first_has_exercise = True
                    lessons.pop(firstindex+1)
            except IndexError:
                pass
            try:
                if lessons[secondindex+1] == com[2] + "-Exercise":
                    second_has_exercise = True
                    lessons.pop(secondindex+1)
            except IndexError:
                pass
            lessons[firstindex], lessons[secondindex] = lessons[secondindex], lessons[firstindex]
            if first_has_exercise:
                lessons.insert(secondindex+1,com[1]+"-Exercise")
            if second_has_exercise:
                lessons.insert(firstindex+1,com[2]+"-Exercise")
    elif com[0]=="Exercise":
        if com[1] in lessons:
            try:
                if lessons[lessons.index(com[1])+1] != com[1]+"-Exercise":
                    lessons.insert(lessons.index(com[1])+1,com[1]+"-Exercise")
            except IndexError:
                lessons.append(com[1]+"-Exercise")
        else:
            lessons.append(com[1])
            lessons.append(com[1]+"-Exercise")

for index, lesson in enumerate(lessons):
    print(f"{index+1}.{lesson}")