""""
Task 6 - Electron Distribution
"""
electrons = int(input())
shell = 0
shells = []
while True:
    shell +=1
    maxnum = 2 * (shell*shell)
    if electrons >= maxnum:
        shells.append(maxnum)
        electrons -= maxnum
    else:
        if electrons != 0:
            shells.append(electrons)
        break
print(shells)