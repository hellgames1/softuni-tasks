""""
Task 5 - Furniture
"""
import re
reg=r">>([a-zA-Z]+)<<([0-9\.]+)!([0-9]+)"
bought=[]
money=0
while True:
    command = input()
    if command=="Purchase":
        break
    matches = re.findall(reg,command)
    if len(matches)>0:
        bought.append(matches[0][0])
        money+=float(matches[0][1])*int(matches[0][2])
print("Bought furniture:")
for i in bought:
    print(i)
print(f"Total money spend: {money:.2f}")