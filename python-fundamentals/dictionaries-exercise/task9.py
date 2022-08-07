""""
Task 9 - Student Activity
"""
dicti={}
newdict={}
count = int(input())
for i in range(count):
    stud = input()
    grad = float(input())
    if stud not in dicti.keys():
        dicti[stud] = [grad]
    else:
        dicti[stud].append(grad)
for i in dicti.keys():
    summ = sum(dicti[i])/len(dicti[i])
    if summ >= 4.5:
        newdict[i]=summ

for let,num in newdict.items():
    print(f"{let} -> {num:.2f}")