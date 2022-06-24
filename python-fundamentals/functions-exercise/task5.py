""""
Task 5 - Even Numbers
"""
nums = [int(a) for a in input().split(" ")]
is_even = lambda a: True if a%2==0 else False
evens = list(filter(is_even,nums))
print(evens)