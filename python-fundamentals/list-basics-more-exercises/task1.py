""""
Task 1 - Zeros to Back
"""
listt = input().split(", ")
zeros=0
output = "["
for item in listt:
    if item!="0":
        output += item + ", "
    else:
        zeros+=1

for i in range(zeros):
    output += "0, "
print(output[:-2]+"]")