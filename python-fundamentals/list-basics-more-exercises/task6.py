""""
Task 6 - List Manipulator
"""
inp = input().split()
listt=[]
for item in inp:
    listt.append(int(item))
while True:
    command = input()
    if command=="end":
        break
    else:
        com = command.split(" ")
    if com[0]=="exchange":
        index=int(com[1])
        if index>=len(listt) or index<0:
            print("Invalid index")
            continue
        sublist = listt.copy()
        listt=listt[:index+1]
        sublist=sublist[index+1:]
        sublist.extend(listt)
        listt=sublist.copy()

        #print(listt)

    elif com[0]=="max":
        max=-1
        index=0
        for i in range(len(listt)):
            if (listt[i]%2 == 0 and com[1]=="odd") or (listt[i]%2 != 0 and com[1]=="even"):
                continue
            if listt[i]>=max:
                max=listt[i]
                index=i
                #print(f"max is {max} at index {i}")
        if max==-1:
            print("No matches")
        else:
            print(index)
    elif com[0]=="min":
        min=9999999999
        index=0
        for i in range(len(listt)):
            if (listt[i]%2 == 0 and com[1]=="odd") or (listt[i]%2 != 0 and com[1]=="even"):
                continue
            if listt[i]<=min:
                min=listt[i]
                index=i
                #print(f"min is {min} at index {i}")
        if min==9999999999:
            print("No matches")
        else:
            print(index)
    elif com[0]=="first":
        howmany = int(com[1])
        if howmany > len(listt):
            print("Invalid count")
            continue
        finds=[]
        for i in range(len(listt)):
            if len(finds)==howmany:
                break
            if (listt[i]%2 == 0 and com[2]=="odd") or (listt[i]%2 != 0 and com[2]=="even"):
                continue
            finds.append(listt[i])
        print(finds)
    elif com[0]=="last":
        howmany = int(com[1])
        if howmany > len(listt):
            print("Invalid count")
            continue
        finds=[]
        for i in range(len(listt)):
            if (listt[i]%2 == 0 and com[2]=="odd") or (listt[i]%2 != 0 and com[2]=="even"):
                continue
            finds.append(listt[i])
        finds.reverse()
        temp = finds[:howmany]
        temp.reverse()
        print(temp)


print(listt)