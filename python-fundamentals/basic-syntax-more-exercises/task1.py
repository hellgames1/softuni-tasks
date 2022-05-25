""""
Task 1 - Find the Largest
"""
num = input()
digits_count = [0,0,0,0,0,0,0,0,0,0]
for digit in num:
    digits_count[int(digit)] += 1
finalnumber = ""
for i in range(10):
    for j in range(digits_count[i]):
        finalnumber = str(i) + finalnumber
print(finalnumber)