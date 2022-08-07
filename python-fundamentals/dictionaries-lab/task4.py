""""
Task 4 - Students
"""
studs={}
while True:
    command = input().split(":")
    if len(command)==1:
        for ind,stud in enumerate(studs):
            if studs[stud][1].lower().replace(" ","_") == command[0]:
                print(f"{stud} - {studs[stud][0]}")
        break
    studs[command[0]]=(command[1],command[2])
#print(studs)