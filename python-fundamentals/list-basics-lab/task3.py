""""
Task 3 - List Statistics
"""
positives = []
negatives = []
sumneg = 0
for i in range(int(input())):
    num = int(input())
    if num>=0:
        positives.append(num)
    else:
        negatives.append(num)
        sumneg += num
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sumneg}")