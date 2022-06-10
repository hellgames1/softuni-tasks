""""
Task 3 - Football Cards
"""
cards = input().split(" ")
teama = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
teamb = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]


if cards!="":
    for card in cards:
        if card in teama:
            teama.remove(card)
        elif card in teamb:
            teamb.remove(card)
        if len(teama) < 7 or len(teamb) < 7:
            break

print(f"Team A - {len(teama)}; Team B - {len(teamb)}")
if len(teama) < 7 or len(teamb) < 7:
    print("Game was terminated")