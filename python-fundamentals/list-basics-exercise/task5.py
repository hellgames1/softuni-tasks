""""
Task 5 - Faro Shuffle
"""
cards = input().split(" ")
halfone = []
halftwo = []
newdeck = []
for j in range(int(input())):
    newdeck = []
    halfone = []
    halftwo = []
    for index, card in enumerate(cards):
        if index < len(cards)/2:
            halfone.append(card)
        else:
            halftwo.append(card)
    for i in range(len(cards)):
        if i % 2 == 0:
            newdeck+=halfone[int(i/2)]
        else:
            newdeck+=halftwo[int(i/2)]
    cards = newdeck
print(cards)