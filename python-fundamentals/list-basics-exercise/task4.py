""""
Task 4 - Number Beggars
"""
ints = []
beggars = []
index=0
done = False
for a in input().split(", "):
    ints.append(int(a))
beggars_count = int(input())
for i in range(beggars_count):
    beggars.append(0)
while not done:
    for i in range(beggars_count):
        try:
            beggars[i]+=ints[index]
        except IndexError:
            done = True
            break
        index+=1
print(beggars)