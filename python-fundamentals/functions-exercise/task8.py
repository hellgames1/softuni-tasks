""""
Task 8 - Palindrome Integers
"""
nums = input().split(", ")
palindrome = lambda a: True if a==a[::-1] else False
for num in nums:
    print(palindrome(num))