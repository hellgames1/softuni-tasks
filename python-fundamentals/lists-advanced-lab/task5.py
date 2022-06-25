""""
Task 5 - Sorting Names
"""
nums = input().split(", ")
print(sorted(names,key=lambda x: (-len(x),x)))