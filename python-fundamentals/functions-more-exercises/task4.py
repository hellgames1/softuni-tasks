""""
Task 4 - Tribonacci Sequence
"""
amount = int(input())
def tribonacci(num):
    lastnums = [0,0,1]
    result=[1]
    for i in range(num-1):
        added = sum(lastnums)
        result.append(added)
        lastnums.pop(0)
        lastnums.append(added)
    return result
print(*tribonacci(amount))