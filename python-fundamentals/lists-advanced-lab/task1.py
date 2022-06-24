""""
Task 1 - No vowels
"""
vowels = list("aoueiAOUEI")
phrase = list(input())
result = [x for x in phrase if x not in vowels]
print("".join(result))