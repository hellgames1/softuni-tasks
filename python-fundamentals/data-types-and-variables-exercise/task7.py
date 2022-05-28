""""
Task 7 - Water Overflow
"""
pours = int(input())
amount = 0
for i in range(pours):
    pour = int(input())
    if pour + amount <= 255:
        amount += pour
    else:
        print("Insufficient capacity!")
print(amount)