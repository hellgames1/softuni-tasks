""""
Task 3 - Wolf in Sheep's clothing
"""
anims = input().split(", ")
if anims[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range(1, len(anims) + 1):
        if anims[-i] == "wolf":
            print(f"Oi! Sheep number {i-1}! You are about to be eaten by a wolf!")
