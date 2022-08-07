""""
Task 12 - SoftUni Exam Results
"""
dicti={}
banned=[]
toprint=[]
while True:
    command = input()
    if command=="exam finished":
        break
    com = command.split("-")
    user = com[0]
    lang = com[1]
    if lang!="banned":
        pts = com[2]
        if lang not in dicti.keys():
            if user not in banned:
                dicti[lang]=[1,(user,pts)]
        else:
            dicti[lang][0]+=1
            if user not in banned:
                userin = (False,-1)
                for index,i in enumerate(dicti[lang]):
                    if index==0:
                        continue
                    if i[0]==user:
                        userin=(True,index)
                if userin[0]:
                    oldpts = dicti[lang][userin[1]][1]
                    if pts > oldpts:
                        dicti[lang][userin[1]] = (user,pts)
                else:
                    dicti[lang].append((user,pts))
    else:
        for current_lang in dicti.keys():
            for index, i in enumerate(dicti[current_lang]):
                if index == 0:
                    continue
                if i[0] == user:
                    dicti[current_lang].pop(index)
                    if user not in banned:
                        banned.append(user)
                    break
print("Results:")
for current_lang in dicti.keys():
    for i in dicti[current_lang]:
        if type(i) is not int:
            already=False
            for ind,item in enumerate(toprint):
                if item[0]==i[0]:
                    already=True
                    if item[1] < i[1]:
                        toprint[ind]=(i[0],i[1])
            if not already:
                toprint.append((i[0],i[1]))
for i in toprint:
    print(f"{i[0]} | {i[1]}")
print("Submissions:")
for current_lang in dicti.keys():
    print(f"{current_lang} - {dicti[current_lang][0]}")