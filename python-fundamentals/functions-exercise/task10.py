""""
Task 10 - Perfect Number
"""
number = int(input())
perfect = lambda num: "We have a perfect number!" if sum([a for a in range(1, num // 2 + 1) if num % a == 0]) == num else "It's not so perfect."

print(perfect(number))