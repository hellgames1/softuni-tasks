""""
Task 3 - Car Race
"""
track = input().split(" ")
track2 = track.copy()
track2.reverse()
length = len(track)
ltime=0
rtime=0

for i in range(length//2 + 1):
    track.pop()
    track2.pop()

length = len(track)
for i in range(length):
    if track[i]=="0":
        ltime*=0.8
    else:
        ltime+=int(track[i])
    if track2[i]=="0":
        rtime*=0.8
    else:
        rtime+=int(track2[i])
if ltime>rtime:
    print(f"The winner is right with total time: {rtime:.1f}")
else:
    print(f"The winner is left with total time: {ltime:.1f}")